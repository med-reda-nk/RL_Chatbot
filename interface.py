import streamlit as st
import base64
import os  # Used for file checking/reading

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Stan - RL Specialist AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --- FUNCTION 1: Handle File Downloading ---
def get_file_content_as_bytes(file_path):
    try:
        if not os.path.exists(file_path):
            return None
        with open(file_path, "rb") as f:
            return f.read()
    except Exception as e:
        # st.error(f"Error reading file {file_path}: {e}") # Optional: Uncomment for debugging
        return None


# --- FUNCTION 2: Handle Image (Base64 for Custom Styling) ---
def get_base64_of_local_file(image_path):
    """Encodes a local image file to a Base64 string for direct HTML embedding."""
    try:
        with open(image_path, "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data).decode()
            # Assuming PNG, change if necessary
            return f"data:image/png;base64,{encoded}"
    except FileNotFoundError:
        # st.warning(f"Image file not found: {image_path}. Using placeholder instead.")
        return ""

    # --- Prepare image source (Run once) ---


image_path = "rlp.jpg"
base64_image_src = get_base64_of_local_file(image_path)

# --- 2. THEME & STYLING (Dark Theme with Custom Round Image CSS) ---
st.markdown("""
    <style>
    /* 2.1. Global Font and Background Polish */
    .stApp, .stMarkdown {
        font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* 2.2. Header & Titles Refinement for Dark Theme */
    h1 {
        color: #8ab4f8; 
        text-align: left;
        font-weight: 700;
        font-size: 2.8em;
        margin-bottom: 0.1em;
    }
    .stMarkdown p {
        color: #bdc1c6; 
        font-size: 1.1em;
        margin-bottom: 0.5em;
        text-align: left !important;
    }

    /* 🌟 CSS for Round Image (PFP) 🌟 */
    #round-logo-container {
        text-align: center;
        margin-bottom: 10px;
    }

    /* 2.3. Professional Iframe Container (Chatbot Embed) */
    .iframe-container {
        position: relative;
        overflow: hidden;
        padding-top: 65%;
        max-width: 900px;
        min-height: 600px;
        margin: 20px auto;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4); 
        border: 1px solid #3c4043;
        background-color: #1c1c1c; 
    }
    .iframe-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: none;
    }

    /* 2.4. Footer Text Color Adjustment */
    div[data-testid="stStatusWidget"] + div > div {
        color: #9aa0a6 !important;
    }

    /* Custom styling for the download button text if file not found */
    .file-not-found {
        color:#f66; 
        font-size: 0.8em;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR: Focused on Utility and Context ---
with st.sidebar:
    # Image Injection (Round PFP)
    if base64_image_src:
        st.markdown(
            f"""
            <div id="round-logo-container">
                <img src="{base64_image_src}" 
                     style="
                        width: 100px; 
                        height: 100px; 
                        border-radius: 50%; 
                        object-fit: cover;"
                >
            </div>
            """,
            unsafe_allow_html=True
        )

    st.header("Settings")
    st.markdown("---")

    # User Personalization
    user_name = st.text_input("Your Name/Identifier", value="RL Researcher")

    # Contextual Information
    st.markdown("---")
    st.subheader("About Stan")
    st.info("""
    **Stan** is an advanced AI specialized in **Reinforcement Learning (RL)**. 
    Ask complex questions about algorithms (DQN, PPO, SAC), theoretical concepts (MDPs, Bellman Equations), or practical applications (Robotics, Gaming).
    """)

# --- 4. MAIN CONTENT: Clear Hierarchy and Modern Layout ---
with st.container():
    st.title("Stan: The RL Specialist AI")
    st.subheader("Your interactive expert for deep dives into Reinforcement Learning.")
    st.markdown(f"**Hello, {user_name}!** Start your advanced inquiry below.")
    st.markdown("---")

col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
with col2:
    st.subheader("Live Chatbot Interface")
    chatbot_url = "https://cdn.botpress.cloud/webchat/v3.3/shareable.html?configUrl=https://files.bpcontent.cloud/2025/10/21/17/20251021171310-UP6Y6TVO.json"

    st.markdown(f"""
        <div class="iframe-container">
            <iframe src="{chatbot_url}" allowfullscreen></iframe>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")  # CORRECTED: Use st.markdown("---") instead of raw ---

## 📚 Training Material Library 🚀

st.markdown("These core texts were used to train Stan's knowledge base. Download them for deeper technical insight.")
st.markdown("---")

### Core Reinforcement Learning Texts

# --- ROW 1: Sutton & Barto ---
# Use columns to align the File Name, Description, and the Button
c_file, c_desc, c_btn = st.columns([1.5, 3, 1])

# Column 1: File Name
with c_file:
    st.markdown("**RL-Theory-Sutton.pdf**")

# Column 2: Description
with c_desc:
    st.markdown("The foundational text on Reinforcement Learning (Sutton & Barto).")

# Column 3: Download Button
with c_btn:
    file_bytes = get_file_content_as_bytes("rltheorybook_AJKS (1).pdf")
    if file_bytes is not None:
        st.download_button(
            "Download Theory",
            file_bytes,
            file_name="rltheorybook_AJKS (1).pdf",
            mime="application/pdf"
        )
    else:
        st.markdown("<p class='file-not-found'>File not found</p>", unsafe_allow_html=True)

st.markdown("---")  # Separator between entries

# --- ROW 2: PPO Paper ---
c_file, c_desc, c_btn = st.columns([1.5, 3, 1])

# Column 1: File Name
with c_file:
    st.markdown("**RL-Algorithms-PPO.pdf**")

# Column 2: Description
with c_desc:
    st.markdown("Advanced paper on Proximal Policy Optimization (PPO).")

# Column 3: Download Button
with c_btn:
    file_bytes = get_file_content_as_bytes("rl (1).pdf")
    if file_bytes is not None:
        st.download_button(
            "Download PPO",
            file_bytes,
            file_name="rl (1).pdf",
            mime="application/pdf"
        )
    else:
        st.markdown("<p class='file-not-found'>File not found</p>", unsafe_allow_html=True)

st.markdown("---")  # CORRECTED: Use st.markdown("---") instead of raw ---

# 4.3. Footer and Acknowledgement
st.markdown(
    """
    <div style="text-align: center; color: #9aa0a6; font-size: 0.9em;">
        © 2025 Stan RL AI | Powered by Streamlit & Botpress | Developed by M.R. Nkira & A. Elhakioui
        <br>
        *Always verify critical information with primary RL literature.*
    </div>
    """,
    unsafe_allow_html=True
)
