import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Caption Generator", page_icon="🚀", layout="centered")

# --- GEMINI API CONFIGURATION ---
# Yahan apni API Key double quotes ke andar paste karein
API_KEY = "AQ.Ab8RN6LpvuXLPHU9FqzvAZ8qRwgY2VaPXKJORS7XPSMsG9Svqw"

try:
    genai.configure(api_key=API_KEY)
except Exception:
    pass

# Initialize Session States
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "credits" not in st.session_state:
    st.session_state.credits = 3

# --- 1. LOGIN / SIGN-UP SCREEN ---
if not st.session_state.logged_in:
    st.title("🔐 AI Caption Generator")
    st.write("Apne account se login karein ya naya account banayein:")
    
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        login_email = st.text_input("Email", key="login_email")
        login_pass = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login Now"):
            if login_email:
                st.session_state.logged_in = True
                st.session_state.user_email = login_email
                st.success("Login kamyaab raha!")
                st.rerun()
            else:
                st.error("Barah-e-karam apna email darj karein.")
                
    with tab2:
        signup_email = st.text_input("Email", key="signup_email")
        signup_pass = st.text_input("Password", type="password", key="signup_pass")
        if st.button("Create Account"):
            if signup_email:
                st.session_state.logged_in = True
                st.session_state.user_email = signup_email
                st.session_state.credits = 3
                st.success("Account ban gaya! Aap ko 3 free credits mil gaye hain.")
                st.rerun()
            else:
                st.error("Barah-e-karam valid email darj karein.")

# --- 2. MAIN APP (AFTER LOGIN) ---
else:
    # Sidebar
    st.sidebar.write(f"👤 **{st.session_state.user_email}**")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
        
    st.sidebar.markdown("---")
    st.sidebar.subheader("💎 Pro Plan ($9.99/mo)")
    st.sidebar.write("Unlimited AI captions aur advanced features hasil karein!")
    if st.sidebar.button("Upgrade to Pro"):
        st.sidebar.info("Yahan Stripe payment gateway connect hoga!")

    # Main Dashboard
    st.title("✨ AI CAPTION GENERATOR")
    st.write("Your Personal AI Social Media Assistant")
    
    st.write(f"🎁 Free Credits Left: **{st.session_state.credits}/3**")

    topic = st.text_input("Type your post or topic here...", placeholder="E.g., How to start YouTube channel for vlogs")

    if st.button("Generate Post"):
        if st.session_state.credits > 0:
            if topic:
                with st.spinner("AI is generating your unique caption..."):
                    try:
                        # Using gemini-2.5-flash / gemini-1.5-flash model
                        model = genai.GenerativeModel("gemini-1.5-flash")
                        prompt = f"Write an engaging social media caption with emojis and relevant hashtags about: {topic}"
                        response = model.generate_content(prompt)
                        
                        st.session_state.credits -= 1
                        st.success("Here is your AI-generated caption:")
                        st.markdown(response.text)
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.warning("Barah-e-karam pehle koi topic likhein!")
        else:
            st.error("Aap ke tamam free credits khatam ho chuke hain! Pro plan upgrade karein.")
