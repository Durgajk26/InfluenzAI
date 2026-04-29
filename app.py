import streamlit as st

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

if st. button("Generate Caption"):
    st.info("AI is thinking... (we'll connect the real AI in Session 2!)")