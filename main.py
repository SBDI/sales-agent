import json
import uuid

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.messages.tool import ToolMessage

from sales_agent.graph import graph


def set_page_config():
    st.set_page_config(
        page_title="Sales Agent",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def set_page_style():
    st.markdown(
        f"""
        <style>
        {open("assets/style.css").read()}
        </style>
    """,
        unsafe_allow_html=True,
    )


def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "thread_id" not in st.session_state:
        st.session_state.thread_id = str(uuid.uuid4())

    if "pending_approval" not in st.session_state:
        st.session_state.pending_approval = None

    if "config" not in st.session_state:
        st.session_state.config = {
            "configurable": {
                "customer_id": "123456789",
                "thread_id": st.session_state.thread_id,
                "browse_prompt": "What products do you have in stock? ",
                "order_prompt": "I want to place an order for product: ",
                "track_prompt": "What is the status of my order with order ID: ",
                "recommend_prompt": "Can you give me some recommendations based on my previous orders? "
            }
        }
    if "input_value" not in st.session_state:
        st.session_state.input_value = ""
        

def setup_sidebar():
    """Configure the sidebar with agent information and controls."""
    with st.sidebar:
        st.image("assets/avatar.jpg", width=100)        # Add a status indicator
        st.title("Smart Sales Agent")
        st.success("🟢 ------------Ready!------------")
        st.markdown("---")
        if st.button("🔄 Start New Chat", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        
        st.markdown("#### Features")
        if st.button("🛒 Browse Products", use_container_width=True):
            st.session_state.input_value = st.session_state.config["configurable"]["browse_prompt"]
            
        if st.button("📦 Place Order", use_container_width=True):
            st.session_state.input_value = st.session_state.config["configurable"]["order_prompt"]
            
        if st.button("🚚 Track Orders", use_container_width=True):
            st.session_state.input_value = st.session_state.config["configurable"]["track_prompt"]
            
        if st.button("🎯 Get Recommendations", use_container_width=True):
            st.session_state.input_value = st.session_state.config["configurable"]["recommend_prompt"]

        st.markdown("---")
        st.markdown(
            """
            <div class="sidebar-footer">
                <div class="by">
                    by Mohamed BOUABIDI
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )


def display_chat_history():
    """Display the chat history."""
    if not st.session_state.messages:
        st.markdown(
            """
            <div style='text-align: center; padding: 30px;'>
                <h1>👋 Welcome!</h1>
                <p>How can I assist you today?</p>
                 <p>Browse / Recommand products || Place / Track orders</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    for message in st.session_state.messages:
        role = "user" if isinstance(message, HumanMessage) else "assistant"
        with st.chat_message(role):
            st.write(message.content)


def process_events(event):
    """Process events from the graph and extract messages."""
    seen_ids = set()

    if isinstance(event, dict) and "messages" in event:
        messages = event["messages"]
        last_message = messages[-1] if messages else None

        if isinstance(last_message, AIMessage):
            if last_message.id not in seen_ids and last_message.content:
                seen_ids.add(last_message.id)
                st.session_state.messages.append(last_message)
                with st.chat_message("assistant"):
                    st.write(last_message.content)

            if hasattr(last_message, "tool_calls") and last_message.tool_calls:
                return last_message.tool_calls[0]

    return None


def handle_tool_approval(snapshot, event):
    """Handle tool approval process."""
    st.write("⚠️ The assistant wants to perform an action. Do you approve?")

    last_message = snapshot.values.get("messages", [])[-1]

    if (
        isinstance(last_message, AIMessage)
        and hasattr(last_message, "tool_calls")
        and last_message.tool_calls
    ):
        tool_call = last_message.tool_calls[0]
        with st.chat_message("assistant"):
            st.markdown("#### 🔧 Proposed Action")

            with st.expander("View Function Details", expanded=True):
                st.info(f"Function: **{tool_call['name']}**")

                try:
                    args_formatted = json.dumps(tool_call["args"], indent=2)
                    st.code(f"Arguments:\n{args_formatted}", language="json")
                except:
                    st.code(f"Arguments:\n{tool_call['args']}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Approve"):
            with st.spinner("Processing..."):
                try:
                    result = graph.invoke(None, st.session_state.config)
                    process_events(result)
                    st.session_state.pending_approval = None
                    st.rerun()
                except Exception as e:
                    st.error(f"Error processing approval: {str(e)}")

    with col2:
        if st.button("❌ Deny"):
            st.session_state.show_reason_input = True

        if st.session_state.get("show_reason_input", False):
            reason = st.text_input("Please explain why you're denying this action:")
            submit = st.button("Submit Denial", key="submit_denial")
            if reason and submit:
                with st.spinner("Processing..."):
                    try:
                        result = graph.invoke(
                            {
                                "messages": [
                                    ToolMessage(
                                        tool_call_id=last_message.tool_calls[0]["id"],
                                        content=f"API call denied by user. Reasoning: '{reason}'. Continue assisting, accounting for the user's input.",
                                    )
                                ]
                            },
                            st.session_state.config,
                        )
                        process_events(result)
                        st.session_state.pending_approval = None
                        st.session_state.show_reason_input = False
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error processing denial: {str(e)}")


def main():
    set_page_config()
    set_page_style()
    initialize_session_state()
    setup_sidebar()

    display_chat_history()

    if st.session_state.pending_approval:
        handle_tool_approval(*st.session_state.pending_approval)

    # Bind chat input to the session state key
    if prompt := st.chat_input(
        "What would you like to order?", 
        key="chat-input",  # Unique key for the chat input
    ):
        if prompt:
            human_message = HumanMessage(content=prompt)
            st.session_state.messages.append(human_message)
            with st.chat_message("user"):
                st.write(prompt)
            # Clear the input_value after submission
            st.session_state.input_value = ""
            try:
                with st.spinner("Thinking..."):
                    events = list(
                        graph.stream(
                            {"messages": st.session_state.messages},
                            st.session_state.config,
                            stream_mode="values",
                        )
                    )
                    last_event = events[-1]
                    tool_call = process_events(last_event)
                    if tool_call:
                        snapshot = graph.get_state(st.session_state.config)
                        if snapshot.next:
                            for event in events:
                                st.session_state.pending_approval = (snapshot, event)
                                st.rerun()
            except Exception as e:
                st.error(f"Error processing message: {str(e)}")

if __name__ == "__main__":
    main()