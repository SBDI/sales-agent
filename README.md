
# 🛍️ Shopping Assistant


This project implements a **Smart Shopping assistant** using **LangChain**, **LangGraph**, and **Streamlit**, powered by the **Groq API**. fu Sensitive actions, like creating orders, require human approval through a human-in-the-loop mechanism.

<p align="center">
  👉 Check out the <a href="https://smartsalesagent.streamlit.app/">Live App Here !</a> for a demo!
</p>

---

## ✨ Key Features

- **Product Inquiries:** Answer questions about availability, pricing, and stock.
- **Order Placement:** Create new orders with human approval.
- **Order Tracking:** Provide real-time order status updates.
- **Personalized Recommendations:** Suggest products based on purchase history.

---

## 🎯 Use Cases

- **E-commerce:** Streamline customer service and boost sales.
- **Customer Support:** Automate routine tasks with user control.
- **Sales Teams:** Offer personalized product recommendations.

---

## 🛠️ Built With

- **LangChain:** Framework for AI-powered conversations.
- **LangGraph:** Stateful agent workflows.
- **SQLite:** Lightweight database for product and order data.
- **Streamlit:** Interactive web interface.
- **Groq API:** Fast and efficient natural language understanding.

---

## 🗂️ Project Structure

```
sopping-assistant/
├── database/          # Database setup and management
├── shopping_assistant/       # Agent logic and tools
├── app.py            # Streamlit app
├── README.md          # This file
├── requirements.txt   # Project dependencies
└── database_init.py  # Database initialization
```


## 🚀 Get Started

### ⚙️ Prerequisites

- Python 3.12+
- Virtual environment recommended.

### 🛠️ Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/SBDI/shopping-assistant.git
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
   python3 database_init.py
   ```

6. **Run the App:**
   ```bash
   streamlit run app.py
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

## Future Roadmap
- Multi-Agent System

- Specialized agents for returns/refunds

- Supervisor agent for coordination

- Advanced Analytics

- Real-time sales dashboard

- Customer sentiment analysis

- Scalability Improvements

- Redis caching layer

- Async API processing
