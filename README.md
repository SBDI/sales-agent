
![shopping-assistant diagram](https://github.com/user-attachments/assets/2c858c15-b268-49df-8000-25beb292f11c)
# 🛍️ Shopping Assistant


This project implements a **Smart Shopping assistant** using **LangChain**, **LangGraph**, and **Streamlit**, powered by the **Groq API**. fu Sensitive actions, like creating orders, require human approval through a human-in-the-loop mechanism.

<p align="center">
  👉 Check out the <a href="https://shopping-assistant1.streamlit.app/">Live App Here !</a> for a demo!
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
   cd shopping-assistant
   ```

2. **Set Up Virtual Environment:**
- uv is recommended !
   ```bash
   uv venv --python 3.12
   venv\Scripts\activate       # Windows
   source venv/bin/activate    # Linux/Mac       
   ```

3. **Install Dependencies:**
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Configure Environment:**
   - Rename `.env-example` to `.env`.
   - Add your `GROQ_API_KEY` and `LANGCHAIN_API_KEY`.

5. **Initialize Database:**
   ```bash
   python database_init.py
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

## Future Roadmap

- Multi-Agent System
- Modular Reasoning, Knowledge, and Language (MRKL).
- User feedback collection.
- Specialized agents for returns/refunds
- Customer sentiment analysis
- Scalability Improvements
- Redis caching layer
- Async API processing
