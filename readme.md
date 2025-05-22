# 🎬 FindFlix AI – YouTube Video Finder with LLM-Powered Analysis

**FindFlix AI** is a smart Streamlit app that helps you discover the **most relevant and recent YouTube videos** using **text input** (supports both **English and Hindi**) and ranks them using **semantic analysis powered by Groq's LLaMA 3 (70B)** model.

---

## ⚡ What It Does

- Takes a search query via a simple, intuitive UI.
- Retrieves the **top 50 recent YouTube videos** matching the query.
- Applies intelligent filters:
  - Video length between **4 to 20 minutes**
  - **Published in the last 14 days**
- Analyzes video titles using **Groq’s LLaMA 3 (70B)** to understand relevance.
- Displays the **single most relevant video** to your query using LLM scoring.

---

## 🧠 Tech Stack

- **Streamlit** – For the interactive frontend
- **YouTube Data API v3** – To fetch and filter videos
- **Groq (LLaMA 3 - 70B)** – For analyzing video titles semantically
- **Python** – Backend logic
- **isodate** – Duration parsing for YouTube videos
- **python-dotenv** – Secure API key management

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/lihtnes_14/find-flix-ai-groq-llama6383
.git
cd find-flix-ai-groq-llama6383
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the app
```bash
streamlit run app.py
```


