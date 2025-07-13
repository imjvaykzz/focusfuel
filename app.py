import streamlit as st
import random
import time
import datetime
import os

st.set_page_config(page_title="FocusFuel - Study. Feel. Win.", page_icon="🎧", layout="centered")

st.markdown("""
    <style>
    body { background-color: #0f172a; color: white; }
    h1, h2, h3, .stMarkdown { color: #e2e8f0 !important; }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 12px;
        padding: 0.6em 1.5em;
        font-size: 1rem;
    }
    .stTextInput>div>input, .stTextArea textarea {
        background-color: #1e293b;
        color: white;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

quotes = [
    "You better lose yourself in the music, the moment...",
    "You gotta find that inner strength...",
    "Even cracked things can hold light.",
    "Discipline outlasts motivation.",
    "Fall seven times, stand up eight.",
    "Focus. Fight. Finish."
]
music_link = "https://www.youtube.com/watch?v=5qap5aO4i9A"
today = datetime.date.today()

st.title("🎧 FocusFuel")
st.markdown("#### Maximize your study flow with music, motivation, and structure")

st.header("💬 Daily Motivation")
st.info(random.choice(quotes))

st.header("🎶 Focus Music")
st.markdown(f"[🎵 Click to listen while studying]({music_link})")

st.header("⏱️ Pomodoro Timer")
col1, col2 = st.columns(2)
session_duration = col1.selectbox("Focus Time (mins):", [25, 50, 90], index=0)
break_duration = col2.selectbox("Break Time (mins):", [5, 10, 15], index=0)

if st.button("Start Focus Session 🚀"):
    placeholder = st.empty()
    for i in range(session_duration * 60, 0, -1):
        mins, secs = divmod(i, 60)
        placeholder.markdown(f"## ⏳ {mins:02d}:{secs:02d}")
        time.sleep(1)
    st.success("✅ Focus session complete!")

    if st.button("Start Break 🧘"):
        placeholder = st.empty()
        for i in range(break_duration * 60, 0, -1):
            mins, secs = divmod(i, 60)
            placeholder.markdown(f"## 🕒 {mins:02d}:{secs:02d}")
            time.sleep(1)
        st.success("🚀 Break over. Back to work!")

st.header("🧠 Lock In Your Reason")
reason = st.text_input("Why are you studying today?")
if reason:
    st.success(f"🔐 Reason saved: {reason}")
    with open("reasons_log.txt", "a") as f:
        f.write(f"{today} - {reason}\n")

st.header("📝 Today's To-Do List")
tasks_input = st.text_area("Enter tasks (one per line):")

if st.button("Save Tasks ✅"):
    tasks = tasks_input.strip().split("\n")
    st.markdown("### 📋 Your Tasks:")
    for task in tasks:
        st.markdown(f"- [ ] {task}")
    with open("tasks_log.txt", "a") as f:
        f.write(f"{today}\n")
        for task in tasks:
            f.write(f"- {task}\n")

st.header("🔥 Daily Streak Tracker")
streak_file = "streak.txt"

if not os.path.exists(streak_file):
    with open(streak_file, "w") as f:
        f.write(str(today))

with open(streak_file, "r") as f:
    last_logged = datetime.date.fromisoformat(f.read().strip())

if today > last_logged:
    st.success("Streak +1 🔥 Great job showing up today!")
    with open(streak_file, "w") as f:
        f.write(str(today))
elif today == last_logged:
    st.info("✅ You've already logged focus today.")
else:
    st.warning("⚠️ No streak today. Restart your habit!")
