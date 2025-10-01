# app.py

import streamlit as st
from datetime import date
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components
from base64 import b64encode
import base64
import time

# --- Background Image ---
# --- Background Image ---
st.set_page_config(page_title="🎉 Happy Birthday Dyuti 🎂", page_icon="💖", layout="wide")

# 
st.markdown("""
    <style>
    @keyframes floatUpDisappear {
        0% {
            bottom: -100px;
            opacity: 0;
            transform: translateX(-50%) scale(0.5);
        }
        10% {
            opacity: 1;
            transform: translateX(-50%) scale(1.2);
        }
        100% {
            bottom: 120%;
            opacity: 0;
            transform: translateX(-50%) scale(0.8);
        }
    }

    .floating-heart {
        position: fixed;
        bottom: -100px;
        left: 50%;
        font-size: 500px;
        color: #ff4d6d;
        z-index: 9999;
        pointer-events: none;
        animation: floatUpDisappear 5s ease-in-out forwards;
    }
    </style>

    <div class="floating-heart">❤️</div>
""", unsafe_allow_html=True)


def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# --- Page Config ---
set_background("imageonline-co-brightnessadjusted.jpg")

# Page config



# Centered CSS + full layout control
st.markdown("""
    <style>
        body {
            text-align: center;
        }
        .centered-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
            text-align: center;
        }

        .stApp {
            text-align: center;
        }

        .stMarkdown, .stText, .stSubheader, .stTitle, .stCaption {
            text-align: center !important;
        }

        .stSlider > label, .stButton > button {
            margin-left: auto;
            margin-right: auto;
        }

        .stAudio, .stVideo {
            display: flex;
            justify-content: center;
        }

        /* Text color for dark background */
        .stApp, .stMarkdown, .stText, .stSubheader, .stTitle, .stCaption, p, div {
            color: #f0f0f0 !important;
        }

        a {
            color: #a8d0e6 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("💖 🎉 Happy Birthday dyuti 💑")
st.markdown("---")
import datetime
from datetime import datetime
import streamlit as st

# Current datetime
today = datetime.now()

# Set next birthday explicitly
next_birthday = datetime(2026, 10, 2, 0, 0, 0)  # 2nd October 2026 at 00:00

# Calculate time difference
time_remaining = next_birthday - today
days = time_remaining.days
hours, rem = divmod(time_remaining.seconds, 3600)
minutes, seconds = divmod(rem, 60)

# Display countdown
st.markdown(f"""
<div style='text-align: center; font-size: 20px; color: #f63366; margin-top: -10px;'>
🎉 <b>Time left for Dyuti's Birthday:</b><br>
🗓️ {days} Day {hours} hours {minutes} minute {seconds} second ⏳
</div>
""", unsafe_allow_html=True)

# Love Letter
st.subheader("💌 A Love Letter")
st.markdown("""
<div class="centered-container">
<p>
Dear <strong>Babling 💖</strong>,<br><br>

From the moment our paths crossed, you've been the light of my life.<br>
Every day with you is a chapter in the most beautiful story I could ever imagine.<br>
This little app is a glimpse into our journey — the smiles, the memories, the love. 💕<br><br>

With all my heart,<br>
<strong>Subhayan 💖</strong>
</p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

st.subheader("📌 Birth Place")
st.image("birthplace.jpg", caption="Dyuti's Birthplace 🏡", width=1000)


# Auto Image Slideshow
import streamlit as st
from base64 import b64encode

st.subheader("📸 Our Memories")

photo_files = [
   
    ("valentine.jpg", "First Valentine 💘"),
    ("victoria.jpg", "Trip to Victoria Memorial 🌸"),
    ("goofy_selfie.jpg", "Goofy Selfies 😝"),
    ("holi_together.jpg", "Special Holi Moment 🌈🎨"),
    ("official meet with kakima.jpg", "Official Meet with Kakima 🤝"),
    ("dada bday celeb.jpg", "Dada's Birthday Celebration 🎂🎉"),
    ("ganga ghat.jpg", "Ganga Ghat Visit 🌊🌅"),
    ("chaturthi.jpg","Chaturthi Durga Puja 🙏🌺"),
    ("panchami.jpg","Panchami Durga Puja 🪔🌼"),
    ("Sasti.jpg","Sasti Durga Puja 🎶🕉️"),
    ("saptami.jpg","Saptami Durga Puja 🎉🔥"),


]

for i, (img_path, caption) in enumerate(photo_files):
    try:
        with open(img_path, "rb") as img_file:
            img_bytes = img_file.read()
            img_base64 = b64encode(img_bytes).decode("utf-8")
            img_url = f"data:image/jpeg;base64,{img_base64}"

            # Alternate layout
            col1, col2 = st.columns([1, 1])

            if i % 2 == 0:  # Even index → image left, caption right
                with col1:
                    st.markdown(
                        f"""
                        <img src="{img_url}" 
                             style="max-width:100%; height:220px; border-radius:10px; object-fit:cover; 
                                    box-shadow:0 4px 10px rgba(0,0,0,0.2);"/>
                        """,
                        unsafe_allow_html=True
                    )
                with col2:
                    st.markdown(
                        f"""
                        <div style="display:flex; align-items:center; height:220px; text-align:left;">
                            <p style="font-size:16px; font-weight:bold; color:#333; margin:10px;">{caption}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:  # Odd index → caption left, image right
                with col1:
                    st.markdown(
                        f"""
                        <div style="display:flex; align-items:center; height:220px; text-align:right;">
                            <p style="font-size:16px; font-weight:bold; color:#333; margin:10px;">{caption}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                with col2:
                    st.markdown(
                        f"""
                        <img src="{img_url}" 
                             style="max-width:100%; height:220px; border-radius:10px; object-fit:cover; 
                                    box-shadow:0 4px 10px rgba(0,0,0,0.2);"/>
                        """,
                        unsafe_allow_html=True
                    )

    except FileNotFoundError:
        st.error(f"Image not found: {img_path}")



# Map of Places



# Create folium map centered around Kolkata

# Create folium map centered around Kolkata
# Map Section
st.subheader("🗺️ Places We've Been")

st.image("place.jpg", caption="Places we have been together 🏡",width=1000)

# Create and populate the map

st.markdown("---")

st.subheader("📍 Description of the Map")
st.image("source.jpg", caption="Places we have been together 🏡",width=1000)
st.write("""
This map represents a personal educational journey starting from **Home (Sonarpur)** and branching out to key academic milestones:

- 🟠 **St. Stephen's School** in Sonarpur, where Class 10 was completed.
- 🟣 **The Modern Academy** in Dhakuria, a transition to higher secondary education.
- 🔵 **Viharilal Home Science Campus** in Alipore, where college-level studies are pursued.

Each route is color-coded to clearly show the path from home to each institution, giving a visual representation of physical distances and directions between important educational stops. This interactive map helps reflect how far one has come — quite literally — in their learning journey.
""")
# Mobile height fix


# Add optional content to fill space & make it feel complete

st.markdown("📸 Stay tuned for more memories and adventures...")

# Optional: Reduce default Streamlit padding
st.markdown("""
    <style>
        .block-container {
            padding-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown("---")
# Timeline
st.subheader("🗓️ Our Love Timeline")
timeline = {
    "2025-01-06": "💘 We met for the first time",
    "2025-02-10": "🌆 First official outing",
    "2025-02-14": "🌸 First Valentine Together",
    "2025-02-15": "💍 First Proposal",
    "2025-02-19": "🌿 Rabindra Sarobar visit",
    "2025-03-03": "💝 Date in Southcity",
    "2025-03-11": "🎨🎄 First Holi",
    "2025-03-25": "🌺 Botanical Garden visit",
    "2025-05-05": "👩‍❤️‍👨 Kamolika didi meet with us",
    "2025-05-10": "🏛️ Jorasanko visit",
    "2025-06-05": "🌊 Ganga Ghat visit",
    "2025-06-22": "👗👕 First twinning dress",
    "2025-06-23": "🎂 Dada bday celebration",
    "2025-06-27": "👩‍👩‍👦 First official outing with Kakima",
    "2025-07-22": "🎬🍿 First movie date",
    "2025-09-24": "Chaturthi Durga Puja 🙏🌺",
    "2025-09-25":"Panchami Durga Puja 🪔🌼",
    "2025-09-26":"Sasti Durga Puja 🎶🕉️",
    "2025-09-27":"Saptami Durga Puja 🎉🔥"
}

for d, event in sorted(timeline.items()):
    st.markdown(f"**{d}** — {event}")

st.markdown("---")

# Playlist
st.subheader("🎶 Our Songs")
st.markdown("""
- Special birthday song for you  
""")
st.audio("Happy Birthday My Love.mp3", format="audio/mp3")
st.markdown("---")

st.markdown("""
<h2 style='color:#ff4b4b; font-family:Georgia;'>
💖 Reason Why She Loves Me 💖
</h2>
""", unsafe_allow_html=True)
st.write('''I have never directly talked to anyone with my family in this way before… but when I started talking with you, everyone in my family began to love you even more than me and started trusting you… You know, I cannot stay happy anywhere without you. While walking on the road, many times I slip or stumble, but even then my eyes look towards you… I have never loved anyone like this before.

When we fight, I have never cried for more than 20 minutes for anyone… I used to show more stubbornness… but even when I get angry, when we argue, I still keep looking at your face.

I feel so good when I go somewhere with my mother… she asks me, “Where is LB, what is he doing?”

My brother never goes out with anyone—not even with his own friends. I have never seen him go out during Puja since childhood. But with you, I have seen him becoming so comfortable…

We have many people in our house… like my aunt’s daughters, Bulti, Didi, and others—I have always seen him speak with them carefully, measuring his words, as if putting on another version of himself. But the way I have seen him with you—just like he is with me, with father, and with mother—that is something different.

Whenever I went out on the road, in any problem, I have found you by my side. You have stood beside me both in respect and in disrespect.

Even when there was no plan to meet my friends, and I never carried any extra money from home—just managed with whatever I had—you were there. That day, when you gave me a signal, I was there.

Those friends are my very old ones… but you manage everything so beautifully, you make me feel complete.

I have seen you—just so that I don’t feel pain—you keep many things inside yourself, manage everything with your own hands, balance everything.

Sometimes I get angry and in the middle of it I don’t say the truth… but you know, I can’t tolerate lies. Why should anything be hidden? I also tend to overthink about all this. And behind this, there’s a big reason which even I know you have… so that I don’t get hurt after hearing it.

Yesterday when you went out with me, I know mother didn’t know. I could catch it from our conversations. And you managed it all so beautifully.''')
# Video
st.markdown("""
<h2 style='color:#ff4b4b; font-family:Georgia;'>
💖 Reason Why I Love Her 💖
</h2>
""", unsafe_allow_html=True)
st.write('''I hope this letter finds you smiling, just the way you always do—the kind of smile that has unknowingly captured my heart from the very beginning.

I don’t even know how to begin expressing everything I feel, but let me try to put it into words, slowly, sincerely—just the way I’ve felt them since 2024. That was the year when my heart first took notice of you. Quietly, gently, and without expecting anything in return, I started liking you. I asked you to meet a few times, but it never worked out. Maybe there were reasons, maybe life just had its own timing—but strangely, my feelings never faded. They only grew stronger.

Though we barely had long conversations on Instagram, I always waited for your replies. Every small interaction, no matter how short, mattered to me. Then came the day—January 6, 2026—a day I will never forget. That sudden, unexpected meeting in Garia… I still remember how time stopped for a moment when I saw you. You looked so stunning, so effortlessly beautiful, that I was genuinely shocked. I had imagined meeting you so many times, but nothing compared to that moment.

After that day, everything began to change—quietly, beautifully. We started meeting more often in Garia, after your college. Those long walks to Kamalgazi, the conversations we shared—funny, deep, random—they brought us closer. What was once a distant admiration slowly turned into a real connection, a friendship that bloomed with time.

And then something happened that touched me in a way I can’t fully explain. The day you called my mother “Mom”… that moment hit differently. It wasn’t just a word—it was full of emotion, warmth, and respect. It showed me your heart. I have never seen anyone do that before. That single act made me realize that my feelings for you weren’t just a passing emotion. I had fallen in love—with who you are, with your soul, with your kindness.

There are so many reasons why I love you—and not just the ones I’ve mentioned. I love the way your eyes light up when you talk about something you’re passionate about. I love your honesty, your simplicity, and the way you carry yourself without trying to impress anyone. I love the way you listen, the way you care, and how you treat everyone with respect.

And if I may say so, a boy often loves a girl not just because of beauty, but because of how she makes him feel—seen, heard, and understood. You made me feel all of that. You made me feel at home.

You might not know the depth of what you mean to me. But every step I’ve taken toward you has been real, and from the heart. This letter isn’t just to tell you that I love you—but to tell you why I love you, and how much you matter to me.

With all my heart 💖''')
st.markdown("""
<h2 style='text-align: center; color: #FF914D; font-family: "Trebuchet MS", sans-serif;'>
🍛 My Love All-Time Favorite Food: <span style="color:#FF4B4B;">Biryani</span> 😋
</h2>
""", unsafe_allow_html=True)
st.image("favfood.jpg", caption="Favourite Food",width=1000)
st.markdown("""
<h2 style='text-align: center; color: #FF914D; font-family: "Trebuchet MS", sans-serif;'>
🍛 My Love  Favorite Flower: <span style="color:#FF4B4B;">Jui</span> 🌺
</h2>
""", unsafe_allow_html=True)
st.image("jui.jpg", caption="Favourite Flower",width=1000)
st.markdown("""
<h2 style='text-align: center; color: #FF914D; font-family: "Trebuchet MS", sans-serif;'>
🍛 My Love  Favorite Singer: <span style="color:#FF4B4B;">as follows:</span> 🌺
</h2>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

# Add images to each column
with col1:
    st.image("KK-11.jpg", caption="KK")

with col2:
    st.image("ar.jpg", caption="Arijit Singh")

with col3:
    st.image("Amaal_Mallik.jpg", caption="Amaal Mallik")
st.subheader("🎥 A Video Just for You")
st.markdown("Here's something special I made with all my heart...")

try:
    video_file = open('specialvideo.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
except FileNotFoundError:
    st.warning("Video file not found. Please place your video in the 'videos' folder.")
st.markdown("---")

# Surprise
st.subheader("🎁 A Special Surprise")
if st.button("Click to Reveal"):
    st.balloons()
    st.success("You are the best part of my every day. Happy Birthday Dyuti❤️.Last but not the least I love you.")

# Footer

# Footer
st.markdown("---")
st.caption("Made with ❤️ love by [Sonai ❤️]")