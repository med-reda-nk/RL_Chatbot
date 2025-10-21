import streamlit as st

# Set page configuration for a wide layout and custom theme for elegance
st.set_page_config(
    page_title="Stan",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for elegant styling: soft gradients, modern fonts, and responsive design
st.markdown("""
    <style>
    /* Global styles */
    body {
        background-color: #f0f4f8;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stApp {
        background: linear-gradient(to bottom right, #e3f2fd, #bbdefb);
    }
    /* Header styling */
    h1 {
        color: #1e88e5;
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 0.5em;
    }
    p {
        color: #424242;
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 2em;
    }
    /* Iframe container for responsive embedding */
    .iframe-container {
        position: relative;
        overflow: hidden;
        padding-top: 56.25%; /* 16:9 Aspect Ratio for responsiveness */
        max-width: 800px;
        margin: 0 auto;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        background-color: white;
    }
    .iframe-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: none;
    }
    /* Sidebar styling for personalization */
    .css-1lcbmhc {
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
        padding: 1em;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for personalized modifications: Add user info or settings
st.sidebar.title("Chatbot Settings")
st.sidebar.markdown("Customize your experience:")
user_name = st.sidebar.text_input("Your Name", value="User")
theme = st.sidebar.selectbox("Theme", ["Light", "Dark"], index=0)
st.sidebar.info("This is a Reinforcement Learning (RL) specialist chatbot. Ask questions about RL algorithms, applications, and more!")

# Main content
st.title("Stan - RL Specialist Chatbot")
st.markdown("Interact with our advanced Reinforcement Learning expert. Get insights, code examples, and advice tailored to your queries.")

# Embed the Botpress chatbot using an iframe in a responsive container
chatbot_url = "https://cdn.botpress.cloud/webchat/v3.3/shareable.html?configUrl=https://files.bpcontent.cloud/2025/10/21/17/20251021171310-UP6Y6TVO.json"
st.markdown(f"""
    <div class="iframe-container">
        <iframe src="{chatbot_url}" allowfullscreen></iframe>
    </div>
""", unsafe_allow_html=True)

# Personalized greeting below the chat for elegance
st.markdown(f"### Welcome, {user_name}! Start chatting in the window above.")
if theme == "Dark":
    st.markdown("<p style='color: #ffffff;'>Dark theme selected for a sleek look.</p>", unsafe_allow_html=True)
else:
    st.markdown("<p>Light theme for a clean interface.</p>", unsafe_allow_html=True)

# Footer for additional elegance
st.markdown("---")

st.markdown("<p style='text-align: center; color: #757575;'>Powered by Streamlit & Botpress | Customized for RL Enthusiasts | Mohamed Reda Nkira - Asmae Elhakioui</p>", unsafe_allow_html=True)
