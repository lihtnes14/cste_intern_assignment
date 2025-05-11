# 🔍 YouTube Video Finder with Analysis

A **Streamlit app** that lets you search for recent and relevant YouTube videos using **text input** (Hindi/English supported) and recommends the **best video** using **Groq's LLaMA 3 model**.

## ⚡ What it does

- Accepts a user search query (text) through a simple UI.
- Searches YouTube for the top 50 recent videos matching the query.
- Filters:
  - Only videos between **4 to 20 minutes**
  - **Published in the last 14 days**
- Analyzes video titles using **Groq's LLaMA 3 (70B)**.
- Returns and displays the **most relevant video** to the user’s query.

---

## 🧠 Powered by

- **Streamlit** – for the interactive UI
- **YouTube Data API v3** – for fetching relevant videos
- **Groq (LLaMA 3 - 70B)** – for semantic analysis of video titles
- **Python** – for backend logic
- **isodate** – to handle YouTube video durations
- **dotenv** – to manage API keys securely

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/youtube-video-finder.git
cd youtube-video-finder
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
### 4. Set up .env

key=YOUR_YOUTUBE_API_KEY
GROQ_API_KEY=YOUR_GROQ_API_KEY

### 5. Run the app
```bash
streamlit run app.py
```


