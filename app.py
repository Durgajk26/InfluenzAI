import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
st.set_page_config(
    page_title="InfluenzAI",
    page_icon="🎯",
    layout="wide"
)

st.title("InfluenzAI")
st.caption("Your AI-powered influencer command centre")

st.divider()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Followers", value="124K", delta="+2.3%")
with col2:
    st.metric(label="Engagement Rate", value="6.8%", delta="+0.4%")

with col3:
    st.metric(label="Posts This Month", value="48")

with col4:
    st.metric(label="Avg Reach", value="3.2K", delta="+12%")

st.divider()
st.subheader("AI Suggestions")

suggestions = [
    ("Best time to post today", "Your audience is most active at 7–9 PM. Post at 7:30 PM for max reach.", "High Impact"),
    ("Try a Reel this week", "Your last 3 Reels got 2x more reach than static posts.", "Trending"),
    ("Refresh your hashtags", "You've used the same hashtags for 2 weeks. Rotate them!", "Action Needed"),
]
for title, tip, tag in suggestions:
    with st.container(border=True):
        st.markdown(f"**{title}** — `{tag}`")
        st.caption(tip)

st.divider()
st.subheader("AI Caption Generator")
niche = st. selectbox("Your niche", ["Lifestyle", "Tech", "Fitness", "Food", "Travel", "Fashion"])
platform = st.selectbox("platform", ["Instagram", "TikTok", "LinkedIn", "YouTube"])
mood = st.selectbox("Caption mood", ["Motivational", "Funny", "informative", "Personal"])

if st.button("Generate Caption"):
    with st.spinner("AI is thinking..."):
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        
        prompt = f"Write 3 creative {mood} captions for a {niche} influencer on {platform}. Include relevant hashtags. Keep each caption under 150 words."
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        caption = response.choices[0].message.content
        st.success("Here are your AI-generated captions!")
        st.write(caption)