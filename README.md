# STAN - RL Specialist Chatbot – Streamlit Web App

A professional Streamlit web application featuring **Stan**, an advanced AI specialized in **Reinforcement Learning (RL)**. The app integrates a Botpress chatbot with a comprehensive training material library and modern dark-themed UI.

 [View Presentation](https://www.canva.com/design/DAG6jvsKCGA/8EDxkrhjwT3ZMf0WedG_XQ/edit?utm_content=DAG6jvsKCGA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

---

## Features

- **Interactive RL Specialist Chatbot** – Ask complex questions about RL algorithms (DQN, PPO, SAC), theoretical concepts (MDPs, Bellman Equations), and practical applications
- **Training Material Library** – Direct download access to foundational RL texts:
  - Sutton & Barto's "Reinforcement Learning: An Introduction"
  - PPO (Proximal Policy Optimization) research paper
- **Modern Dark Theme UI** with professional styling:
  - Rounded profile picture display
  - Elegant iframe container with shadows
  - Responsive design optimized for all screen sizes
- **Customizable Sidebar**:
  - User name/identifier input for personalized greeting
  - About section with Stan's capabilities
  - Settings panel
- **Mobile-Friendly** – Fully responsive layout with centered containers
- **Professional Footer** – Copyright and acknowledgment section

---

## How to Run Locally

### Prerequisites
- Python 3.8+
- `streamlit` installed

### 1. Clone or Download the Project
```bash
git clone https://github.com/med-reda-nk/RL_Chatbot.git
cd RL_Chatbot
```

### 2. Install Dependencies
```bash
pip install streamlit
```

### 3. Prepare Required Files
Ensure these files are in the project directory:
- `rlp.jpg` – Stan's profile picture (round logo)
- `rltheorybook_AJKS (1).pdf` – Sutton & Barto RL textbook
- `rl (1).pdf` – PPO algorithm paper

### 4. Run the App
```bash
streamlit run interface.py
```
The app will open in your browser at `http://localhost:8501`

---

## Project Structure

```
rl-chatbot-streamlit/
│
├── interface.py                  # Main Streamlit application
├── README.md                     # This file
├── rlp.jpg                       # Stan's profile picture (round logo)
├── rltheorybook_AJKS (1).pdf     # Sutton & Barto RL textbook
├── rl (1).pdf                    # PPO algorithm paper
└── requirements.txt              # Python dependencies
```

---

## Key Components

### 1. **Configuration**
```python
st.set_page_config(
    page_title="Stan - RL Specialist AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)
```

### 2. **Sidebar Features**
- **Round Profile Picture** – Displays Stan's avatar using Base64 encoding
- **User Name Input** – Personalize your experience
- **About Section** – Information about Stan's RL expertise

### 3. **Main Content**
- **Welcome Header** – Personalized greeting with user name
- **Embedded Chatbot** – Responsive iframe with professional styling
- **Training Material Library** – Download buttons for RL resources

### 4. **File Download System**
The app includes a robust file handling system:
```python
def get_file_content_as_bytes(file_path):
    # Reads files and returns bytes for download
    # Handles missing files gracefully
```

---

## Customization Guide

### Change the Chatbot
Edit the Botpress URL in `interface.py`:
```python
chatbot_url = "https://cdn.botpress.cloud/webchat/v3.3/shareable.html?configUrl=https://files.bpcontent.cloud/2025/10/21/17/20251021171310-UP6Y6TVO.json"
```

### Modify Styling
All custom CSS is in the `st.markdown("""<style>...`)` block. Key customization areas:

**Colors:**
```css
h1 { color: #8ab4f8; }  /* Header color */
.stMarkdown p { color: #bdc1c6; }  /* Text color */
```

**Profile Picture:**
```css
#round-logo-container img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
}
```

**Iframe Container:**
```css
.iframe-container {
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    background-color: #1c1c1c;
}
```

### Add More Training Materials
Add new download sections by copying this pattern:
```python
c_file, c_desc, c_btn = st.columns([1.5, 3, 1])

with c_file:
    st.markdown("**Your-File-Name.pdf**")

with c_desc:
    st.markdown("Description of the resource.")

with c_btn:
    file_bytes = get_file_content_as_bytes("your-file.pdf")
    if file_bytes is not None:
        st.download_button(
            "Download",
            file_bytes,
            file_name="your-file.pdf",
            mime="application/pdf"
        )
```

---

## Deployment Options

| Platform                          | One-Click Deploy | Notes                          |
|-----------------------------------|------------------|--------------------------------|
| **Streamlit Community Cloud**     | ✅ Yes           | Easiest option (free)          |
| **Heroku**                        | ✅ Yes           | Requires Procfile              |
| **Render**                        | ✅ Yes           | Auto-deploys from GitHub       |
| **Docker**                        | ✅ Yes           | Use streamlit Docker image     |
| **AWS/GCP/Azure**                 | ⚙️ Manual        | Full control, more setup       |

### Deploy to Streamlit Community Cloud
1. Push code to GitHub (ensure all files are included)
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Connect your GitHub repository
5. Select `interface.py` as the main file
6. Deploy! 

**Important:** Make sure `rlp.jpg` and PDF files are committed to the repository.

---

## Requirements

Create a `requirements.txt` file:
```txt
streamlit==1.31.0
```

For development:
```txt
streamlit==1.31.0
pillow  # If you plan to process images
```

---

## Tech Stack

- **[Streamlit](https://streamlit.io)** – Web application framework
- **[Botpress Cloud](https://botpress.com)** – AI chatbot platform (v3.3 Webchat)
- **HTML/CSS** – Custom dark theme styling
- **Base64 Encoding** – For embedded profile picture
- **Python 3.8+** – Backend logic

---

## Features in Detail

### File Download System
- **Graceful Error Handling** – Shows "File not found" message if PDFs are missing
- **Secure File Reading** – Uses context managers for safe file operations
- **MIME Type Support** – Proper PDF content type for downloads

### Responsive Design
- **Wide Layout** – Maximizes screen real estate
- **Column-Based Layout** – Clean organization of download sections
- **Mobile Optimization** – Iframe adapts to screen size

### Professional UI Elements
- **Round Profile Picture** – Modern avatar display
- **Centered Iframe** – Professional chatbot container
- **Consistent Spacing** – `st.markdown("---")` separators
- **Color-Coded Text** – Visual hierarchy with custom colors

---

## Troubleshooting

### Chatbot Not Loading
- Check internet connection
- Verify Botpress URL is correct
- Try accessing the URL directly in browser

### Files Not Downloading
- Ensure PDF files exist in project directory
- Check file names match exactly (case-sensitive)
- Verify file permissions

### Profile Picture Not Showing
- Confirm `rlp.jpg` exists in project root
- Check file format (should be .jpg or .png)
- Verify file is not corrupted

---

## Contributing

Contributions are welcome! Feel free to:
- Report bugs via GitHub Issues
- Suggest new features
- Propose UI/UX improvements
- Improve documentation
- Submit pull requests

---

## License

MIT License – Feel free to use, modify, and distribute.

---

## Authors

**Mohamed Reda Nkira** & **Asmae Elhakioui** & **Mouhcine Zouga**   
Engineering Students | IATD-SI  

- [GitHub - Mohamed Reda Nkira](https://github.com/med-reda-nk)  
- [LinkedIn - Mohamed Reda Nkira](https://www.linkedin.com/in/mohamed-reda-nkira-5691432a3)

---

## Acknowledgments

- **Sutton & Barto** – For the foundational RL textbook
- **Botpress** – For the powerful chatbot platform
- **Streamlit** – For the amazing web framework
- **RL Community** – For continuous innovation in reinforcement learning

---

## Screenshots

*(Add screenshots here after deployment)*

1. **Main Interface** – Dark theme with chatbot
2. **Sidebar** – User settings and about section
3. **Training Library** – Download section for RL materials
