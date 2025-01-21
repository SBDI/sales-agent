import os
from datetime import datetime
from typing import Annotated

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableConfig
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import AnyMessage, add_messages
from langgraph.prebuilt import tools_condition
from typing_extensions import TypedDict
from langchain_groq import ChatGroq  # Import ChatGroq

from sales_agent.tools import (
    check_order_status,
    create_order,
    get_available_categories,
    search_products,
    search_products_recommendations,
)
from sales_agent.utils import create_tool_node_with_fallback

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY") # Added this line

class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    user_info: str

class Assistant:
     def __init__(self, runnable: Runnable):
        self.runnable = runnable

     def __call__(self, state: State, config: RunnableConfig):
         while True:
            configuration = config.get("configurable", {})
            customer_id = configuration.get("customer_id", None)
            state = {**state, "user_info": customer_id}
            result = self.runnable.invoke(state)
            # If the LLM happens to return an empty response, we will re-prompt it
            # for an actual response.
            if not result.tool_calls and (
                not result.content
                or isinstance(result.content, list)
                and not result.content[0].get("text")
            ):
                messages = state["messages"] + [("user", "Respond with a real output.")]
                state = {**state, "messages": messages}
            else:
                break
         return {"messages": result}


llm = ChatGroq(model="llama-3.3-70b-versatile")  # Modified this line

assistant_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful virtual sales assistant for our online store. Your goal is to provide excellent customer service by helping customers find products, make purchases, and track their orders.

... (rest of the system prompt) ...
        """,
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now)

assistant_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful virtual sales assistant for our online store. Your goal is to provide excellent customer service by helping customers find products, make purchases, and track their orders.

Use the provided tools to:
- Search for products and provide relevant recommendations
- See available product categories
- Process customer orders efficiently
- Track order status and provide updates
- Guide customers through their shopping experience

When searching for products:
- Be thorough in understanding customer needs and preferences
- If specific products aren't found, suggest similar alternatives
- Use the get product categories tool to help customers explore options
- Use category and price range flexibility to find relevant options if the customer provides this information
- Provide detailed product information including price, availability in bullet points style.

When making recommendations:
- Consider customer's past purchases and preferences
- Suggest complementary products when appropriate
- Focus on in-stock items
- Explain why you're recommending specific products

When handling orders:
- Verify product availability before confirming orders
- Clearly communicate order details and total costs
- Provide order tracking information
- Keep customers informed about their order status

Always maintain a friendly, professional tone and:
- Ask clarifying questions when needed
- Provide proactive suggestions
- Be transparent about product availability and delivery times
- Help customers find alternatives if their first choice is unavailable
- Follow up on order status proactively
- Explain any limitations or restrictions clearly

If you can't find exactly what the customer is looking for, explore alternatives and provide helpful suggestions before concluding that an item is unavailable.

\n\nCurrent user:\n<User>\n{user_info}\n</User>
\nCurrent time: {time}.""",
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now)

# "Read"-only tools
safe_tools = [
    get_available_categories,
    search_products,
    search_products_recommendations,
    check_order_status,
]

# Sensitive tools (confirmation needed)
sensitive_tools = [
    create_order,
]

sensitive_tool_names = {tool.name for tool in sensitive_tools}

assistant_runnable = assistant_prompt | llm.bind_tools(safe_tools + sensitive_tools)

builder = StateGraph(State)


# Define nodes: these do the work
builder.add_node("assistant", Assistant(assistant_runnable))
builder.add_node("safe_tools", create_tool_node_with_fallback(safe_tools))
builder.add_node("sensitive_tools", create_tool_node_with_fallback(sensitive_tools))


def route_tools(state: State):
    next_node = tools_condition(state)
    # If no tools are invoked, return to the user
    if next_node == END:
        return END
    ai_message = state["messages"][-1]
    # This assumes single tool calls. To handle parallel tool calling, you'd want to
    # use an ANY condition
    first_tool_call = ai_message.tool_calls[0]
    if first_tool_call["name"] in sensitive_tool_names:
        return "sensitive_tools"
    return "safe_tools"


# Define edges: these determine how the control flow moves
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant", route_tools, ["safe_tools", "sensitive_tools", END]
)
builder.add_edge("safe_tools", "assistant")
builder.add_edge("sensitive_tools", "assistant")

# Compile the graph
memory = MemorySaver()
graph = builder.compile(checkpointer=memory, interrupt_before=["sensitive_tools"])
