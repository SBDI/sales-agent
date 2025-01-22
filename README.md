
# 🛍️ Smart Sales Agent


This project implements a **Smart Sales Agent** using **LangChain**, **LangGraph**, and **Streamlit**, powered by the **Groq API**. The agent assists customers with product inquiries, order placement, order tracking, and personalized recommendations. Sensitive actions, like creating orders, require human approval through a human-in-the-loop mechanism.

<p align="center">
  👉 Check out the <a href="Streamlit hosted Agent">Live App Here !</a> for a demo!
</p>

---

## 📑 Table of Contents
1. [✨ Key Features](#key-features)
2. [🛠️ Built With](#built-with)
3. [🎯 Use Cases](#use-cases)
4. [🗂️ Project Structure](#project-structure)
5. [🚀 Get Started](#get-started)
6. [🔗 Related Resources](#related-resources)
7. [🔮 Future Plans](#future-plans)

---

## ✨ Key Features

- **Product Inquiries:** Answer questions about availability, pricing, and stock.
- **Order Placement:** Create new orders with human approval.
- **Order Tracking:** Provide real-time order status updates.
- **Personalized Recommendations:** Suggest products based on purchase history.

---

## 🛠️ Built With

- **LangChain:** Framework for AI-powered conversations.
- **LangGraph:** Stateful agent workflows.
- **SQLite:** Lightweight database for product and order data.
- **Streamlit:** Interactive web interface.
- **Groq API:** Fast and efficient natural language understanding.

---

## 🎯 Use Cases

- **E-commerce:** Streamline customer service and boost sales.
- **Customer Support:** Automate routine tasks with user control.
- **Sales Teams:** Offer personalized product recommendations.

---

## 🗂️ Project Structure

```
sales_agent/
├── database/          # Database setup and management
├── sales_agent/       # Agent logic and tools
├── main.py            # Streamlit app
├── README.md          # This file
├── requirements.txt   # Project dependencies
└── setup_database.py  # Database initialization
```

---

## 🚀 Get Started

### ⚙️ Prerequisites

- Python 3.12+
- Virtual environment recommended.

### 🛠️ Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/SBDI/sales-agent.git
   cd sales-agent
   ```

2. **Set Up Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate       # Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment:**
   - Rename `.env-example` to `.env`.
   - Add your `GROQ_API_KEY` and `LANGCHAIN_API_KEY`.

5. **Initialize Database:**
   ```bash
   python3 setup_database.py
   ```

6. **Run the App:**
   ```bash
   streamlit run main.py
   ```

---

## 🔗 Related Resources

- [LangChain Docs](https://python.langchain.com/docs/introduction/)
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
- [Streamlit Docs](https://docs.streamlit.io)
- [Groq API Docs](https://console.groq.com/docs)

---

## 🔮 Future Plans

- Multi agentic system + Agentic RAG.
- Modular Reasoning, Knowledge, and Language (MRKL).
- User feedback collection.
