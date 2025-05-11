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
