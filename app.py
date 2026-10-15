import streamlit as st

st.set_page_config(page_title="AI Caption Generator", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
    }
    .main-title {
        text-align: center;
        font-size: 28px;
        font-weight: 800;
        color: #38bdf8;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        font-size: 14px;
        color: #94a3b8;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

if 'credits' not in st.session_state:
    st.session_state.credits = 3

st.markdown('<p class="main-title">AI CAPTION GENERATOR</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Your Personal AI Social Media Assistant</p>', unsafe_allow_html=True)

topic = st.text_area("Type your post or topic here...", placeholder="E.g., 5 tips to grow on Instagram...")

button_label = f"Generate Post (Free Credits Left: {st.session_state.credits}/3)"

if st.button(button_label, use_container_width=True):
    if st.session_state.credits > 0:
        if topic.strip() == "":
            st.warning("Please type a topic first!")
        else:
            st.session_state.credits -= 1
            with st.spinner("AI is crafting your viral caption..."):
                st.success("✨ Here is your AI-generated caption:")
                st.markdown(f"""
                > **Generated Caption for:** *{topic}*
                > 
                > 🚀 Stop scrolling and read this! If you want to master your niche, you need consistency over perfection. 
                > 
                > Drop a 🔥 if you agree!
                > 
                > #ContentCreator #SocialMedia #Growth #AI
                """)
    else:
        st.error("🚨 Out of Free Credits!")
        st.info("💎 Upgrade to Pro for **$9.99/month** to get unlimited AI generations!")
