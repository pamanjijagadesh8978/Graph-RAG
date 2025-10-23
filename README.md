# Graph-RAG

---

## 🧠 Graph Document Chatbot — Health & Nutrition Advisor

### 🚀 Overview

This project is an **AI-powered chatbot** built with **Streamlit**, **LangChain**, and **Google Gemini 2.5 Flash**, designed to answer user questions using data from a **locally stored Knowledge Graph**.
It functions as a **Health & Nutrition Advisor**, reading structured and unstructured graph data to generate detailed, domain-aware responses.

---

### 🧩 Features

✅ **Knowledge Graph-based context** — Reads `graph_documents.pkl` for domain knowledge.
✅ **Gemini 2.5 Flash Integration** — Fast, cost-efficient reasoning via LangChain’s `ChatGoogleGenerativeAI`.
✅ **Streamlit UI** — User-friendly web app for instant Q&A.
✅ **Fully Local Context** — No vector DB required; operates on serialized graph documents.
✅ **Custom Prompts** — Prevents hallucination by constraining Gemini to provided context.

---

### 🏗️ Architecture

```plaintext
graph_documents.pkl  →  LangChain  →  Gemini 2.5 Flash (LLM)
                               ↓
                        Streamlit Chat UI
```

**Workflow**

1. Load serialized graph documents (`graph_documents.pkl`).
2. Combine contents into a context string.
3. Send both **context** and **user question** to Gemini via LangChain.
4. Streamlit displays the AI’s detailed answer.

---

### 📁 Project Structure

```
GraphDocumentChatbot/
│
├── streamlit_app.py         # Streamlit chatbot frontend + backend
├── KG.ipynb                 # Notebook for creating the knowledge graph
├── graph_documents.pkl      # Preprocessed graph data
├── ChatBot.pdf              # Project summary / documentation
├── requirements.txt         # Dependencies
└── README.md                # This file
```

---

### ⚙️ Installation

#### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/GraphDocumentChatbot.git
cd GraphDocumentChatbot
```

#### 2️⃣ Create & activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```

#### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Add your Google Gemini API key securely

Create a `.streamlit/secrets.toml` file:

```toml
GOOGLE_API_KEY = "your_gemini_api_key_here"
```

---

### ▶️ Running the App

```bash
streamlit run streamlit_app.py
```

Then open the local URL shown (usually `http://localhost:8501`).

---

### 💬 Example Interaction

**User:**

> What are the best protein sources for a vegan diet?

**Chatbot:**

> Based on the knowledge graph, top vegan protein sources include lentils, chickpeas, tofu, quinoa, and nuts.
> Combining plant proteins helps ensure a complete amino acid profile.

---

### 📸 Screenshots

You can include screenshots here (add them to your repo as `images/` folder):

```markdown
### 🖼️ App Interface
![App UI](images/app_ui.png)

### 💬 Example Chat
![Chat Example](images/chat_example.png)
```

*(Replace the file names with your actual screenshot names, e.g., `chat_1.png`, `dashboard.png`.)*

---

### 🧠 Future Enhancements

* Integrate **FAISS / Chroma** for semantic retrieval.
* Connect to **Neo4j / Azure Cosmos DB (Gremlin API)** for live graph queries.
* Add **multi-turn conversation memory** via LangChain.
* Expand dataset to include fitness, lifestyle, and clinical nutrition knowledge.

---

### 🤝 Contributing

Contributions are welcome!
If you’d like to improve knowledge graph creation, retrieval, or UI:

1. Fork the repo
2. Create a feature branch (`feature/add-search`)
3. Commit and push your changes
4. Submit a pull request

---
---

### 🧩 Tech Stack

| Component    | Technology               |
| ------------ | ------------------------ |
| Framework    | Streamlit                |
| LLM          | Google Gemini 2.5 Flash  |
| Middleware   | LangChain                |
| Data Storage | Pickle (Knowledge Graph) |
| Notebook     | Jupyter (KG.ipynb)       |
| Language     | Python 3.10+             |

---
