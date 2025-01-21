# 🛍️ Virtual Sales Agent powered by LangGraph, Streamlit & Groq

<p align="center">
  <img src="./assets/agent_workflow.png" alt="Agent Workflow Diagram" width="500">
</p>

This project implements a **Virtual Sales Agent** that simulates customer interactions, providing information and support through a Streamlit interface. Leveraging the power of **LangChain**, **LangGraph**, and a SQLite database, this agent can answer product questions, create orders, check order statuses, and offer personalized recommendations. These tools are divided into safe and sensitive categories. For sensitive tools, such as creating orders, a human-in-the-loop mechanism is implemented, requiring approval or denial before proceeding. The agent now uses the **Groq API** for natural language understanding, providing fast and efficient responses.

<p align="center">
  👉 Check out a quick demo of the Virtual Sales Agent in action in the <a href="#interface-preview">Interface Preview</a> section!
</p>

---

## 📑 Table of Contents
1.  [✨ Key Features](#key-features)
2.  [🛠️ Built With](#built-with)
3.  [🎯 Use Cases](#use-cases)
4.  [🗂️ Project Structure](#project-structure)
5.  [🖼️ Interface Preview](#interface-preview)
6.  [🚀 Get Started](#get-started)
7.  [🤝 Contributing](#contributing)
8.  [🔗 Related Resources](#related-resources)
9.  [🔮 Future Plans](#future-plans)
10. [📜 License](#license)

---

## ✨ Key Features

This virtual sales agent can assist customers with:

1.  **Product Inquiries:**
    *   🔍 Answer questions about product availability, pricing, and stock levels.
    *   **Example Questions:**
        *   💬 "What products do you have in stock?"
        *   💰 "How much does product X cost?"
        *   📦 "Is product Y available?"

2.  **Order Placement:**
    *   🛒 Allow customers to create new orders, referencing data from the database.
    *   **Example Request:** "I would like to order 2 units of product Z."

3.  **Order Tracking:**
    *   🚚 Provide up-to-date status information for existing orders.
    *   **Example Question:** "What is the status of order #54321?"

4.  **Personalized Recommendations:**
    *   🎯 Suggest relevant products based on a customer's past purchase history.
    *   **Example Recommendation:** "Based on your previous order, you might also like product A."

---

## 🛠️ Built With

*   **LangChain:** 🔗 Provides the framework for developing AI-powered conversational applications.
*   **LangGraph:** 🔗 Enables the creation of sophisticated, stateful agent workflows.
*   **SQLite:** 🗄️ A lightweight database for managing product data and orders.
*   **Streamlit:** 🖥️ Facilitates the development of interactive web applications for the agent interface.
*   **Groq API:** 🚀 A fast and efficient large language model for natural language understanding.

---

## 🎯 Use Cases

This Virtual Sales Agent is ideal for:
*   **E-commerce websites** to streamline customer service and increase sales.
*   **Customer support teams** looking to automate routine tasks while maintaining user control.
*   **Sales teams** to recommend personalized products based on purchase history.

---

## 🗂️ Project Structure

Here's a breakdown of the project's directory structure:

├── assets/
│ ├── agent_workflow.png # Diagram
│ ├── demo.gif # Demo gif
│ ├── graph.png # Agent workflow diagram
│ └── style.css # Streamlit custom styling
├── database/
│ ├── db/
│ │ ├── products.json # Bot product data (initial)
│ │ └── schemas.sql # SQL schema definitions
│ ├── db_manager.py # Handles database interactions
│ └── config.py # Database connection configuration
├── sales_agent/
│ ├── graph.py # LangGraph agent state machine and logic
│ ├── tools.py # Custom tools used by the agent
│ └── utils.py # Utility functions for the agent
├── env-example # Environment variables template
├── main.py # Main Streamlit app
├── README.md # This file!
├── requirements.txt # Project dependencies
└── setup_database.py # Script to initialize the database


---

## 🖼️ Interface Preview

1.  **🎥 Demo GIF**
    Here's a quick demonstration of the Virtual Sales Agent in action:
    *   **Main Interface:** A clean and intuitive chatbot interface that interacts with customers to answer queries and perform tasks.
    *   **Human-in-the-Loop Approval System:** A mechanism where sensitive actions, like order creation, require user approval. Users can review the action details and provide feedback for continuous improvement.

    <p align="center">
      <img src="./assets/demo.gif" alt="Demo GIF" width="600">
    </p>

2.  **LangGraph Workflow**

    <p align="center">
      <img src="./assets/graph.png" alt="Virtual Sales Agent Interaction Flow" width="600" title="Virtual Sales Agent Interaction Flow">
    </p>

---

## 🚀 Get Started

Follow these steps to set up and run the Virtual Sales Agent:

### ⚙️ Prerequisites

*   ✅ Ensure you have **Python 3.12 or later** installed on your machine.
*   🧪 We recommend using a virtual environment for managing dependencies.

### 🛠️ Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/sales-ai-agent-langgraph.git
    cd sales-ai-agent-langgraph
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate    # Linux/Mac
    venv\Scripts\activate       # Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Configuration:**
    *   📝 Rename the `.env-example` file to `.env`.
    *   🔑 Set up your API keys:
        *   **Groq API:** Requires a `GROQ_API_KEY`. Obtain this from your [Groq](https://console.groq.com/) account.
        *   **LangSmith:** Create a [LangSmith](https://smith.langchain.com/) account and get your `LANGCHAIN_API_KEY`. This is for monitoring and debugging agent interactions.
    *   ⚙️ Load environment variables:
        ```bash
        source .env
        ```

5.  **Initialize the Database:**
    ```bash
    python3 setup_database.py
    ```

6.  **Launch the Streamlit App:**
    ```bash
    streamlit run main.py
    ```

    This will open the application in your web browser, and you can start interacting with the Virtual Sales Agent.

---

## 🤝 Contributing

We welcome contributions to improve this project! Here’s how you can help:
1.  🍴 Fork the repository and create a feature branch.
2.  ✍️ Follow Python best practices (e.g., PEP 8).
3.  🚀 Submit a pull request with a clear description of your changes.
4.  🐛 For bug reports or feature requests, please open an issue.

---

## 🔗 Related Resources

*   [LangChain Documentation](https://python.langchain.com/docs/introduction/)
*   [LangGraph Documentation](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
*   [Streamlit Documentation](https://docs.streamlit.io)
*   [Groq API Documentation](https://console.groq.com/docs)

---

## 🔮 Future Plans

- Fuzzy logic for product names matching

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---