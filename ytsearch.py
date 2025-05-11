import streamlit as st
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os 
import datetime
import isodate
from groq import Groq

load_dotenv()
YT_API_KEY = os.getenv("key")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=GROQ_API_KEY)

youtube = build("youtube", "v3", developerKey=YT_API_KEY)

def search_youtube(query):
    published_after = (datetime.datetime.now() - datetime.timedelta(days=14)).isoformat("T") + "Z"

    search_response = youtube.search().list(
        q=query,
        type="video",
        part="snippet",
        maxResults=50,
        publishedAfter=published_after
    ).execute()

    video_ids = [item["id"]["videoId"] for item in search_response["items"]]
    
    if not video_ids:
        return []


    video_details_response = youtube.videos().list(
        part="contentDetails,snippet",
        id=",".join(video_ids)
    ).execute()

    videos = []
    for item in video_details_response.get("items", []):
        duration = item["contentDetails"]["duration"]
        durationsec = isodate.parse_duration(duration).total_seconds()
        if 240 <= durationsec <= 1200:
            title = item["snippet"]["title"]
            video_id = item["id"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            videos.append((title, video_url))
            if len(videos) == 20:
                break

    return videos

def get_best_from_groq(query, video_list):
    prompt = f"""You are an expert video assistant.

The user searched for: "{query}"

Below is a list of YouTube videos (title and URL). Choose the one most relevant to the user's intent and return ONLY the title and URL of the best video.

Videos:
{chr(10).join([f"{i+1}. {title} -> {url}" for i, (title, url) in enumerate(video_list)])}

Reply in this format ONLY:
Title: <title>
URL: <url>
"""
    
    response = groq_client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content


