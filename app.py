import streamlit as st
from ytsearch import search_youtube, get_best_from_groq

st.set_page_config(page_title="YouTube Video Finder with Analysis", layout="centered")
st.title("🔍 YouTube Video Finder with Analysis")
st.write("""
    Welcome to the YouTube Video Finder with Analysis app powered by Groq. 
    Enter a search query below to find relevant YouTube videos and get an analysis of the best match.
    """)

query = st.text_input("🔎 Enter your search query:", placeholder="e. ")

if query:
    with st.spinner("Searching for videos..."):

        videos = search_youtube(query)
        
    if videos:
        with st.spinner("Analyzing the best match..."):
            best_video = get_best_from_groq(query, videos)

        title_start = best_video.find("Title: ") + len("Title: ")
        title_end = best_video.find("\n", title_start)
        title = best_video[title_start:title_end]
        url_start = best_video.find("URL: ") + len("URL: ")
        url = best_video[url_start:].strip()

        st.subheader("🎬 Best Video Selected by Groq:")
        st.write(f"**Title**: {title}")
        st.write(f"**URL**: [Watch here]({url})")
        st.video(url)
        
    else:
        st.error("🚨 No videos found matching your query.")
else:
    st.info("🔍 Start by entering a search query above.")
