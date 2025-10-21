```markdown
# RL Specialist Chatbot – Streamlit Web App

A Streamlit web application that integrates a **Reinforcement Learning (RL) Specialist Botpress Chatbot** using a responsive iframe embed.

---

## Features

- **Fully responsive chatbot embed** with 16:9 aspect ratio
- **Elegant UI/UX** with soft gradients, modern typography, and subtle shadows
- **Customizable sidebar**:
  - Enter your name for a personalized greeting
  - Toggle between **Light** and **Dark** themes (visual feedback)
- **Clean, professional layout** using Streamlit’s wide mode
- **Mobile-friendly** design with centered, rounded iframe container
- Powered by **Botpress Cloud Webchat v3.3**

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

### 3. Run the App

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
├── README.md               # This file
└── requirements.txt
```

---

## Customization Guide

### Change the Chatbot

Edit this line in `interface.py`:

```python
chatbot_url = "https://cdn.botpress.cloud/webchat/v3.3/shareable.html?configUrl=https://files.bpcontent.cloud/2025/10/21/17/20251021171310-UP6Y6TVO.json"
```

Replace with your own Botpress shareable link.

### Modify Styling

All custom CSS is in the `st.markdown("""<style>...`)` block. Adjust:
- Colors (`#1e88e5`, gradients)
- Fonts
- Shadows and border radius
- Sidebar content

### Add More Personalization

- Add avatar upload in sidebar
- Save user preferences with `st.session_state`
- Integrate analytics or logging

---

## Deployment Options

| Platform               | One-Click Deploy |
|------------------------|------------------|
| **Streamlit Community Cloud** | Yes (Connect GitHub) |
| **Heroku / Render**    | Yes              |
| **Docker**             | Yes              |

### Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. New app → Select repo → Deploy!

---


## Tech Stack

- **[Streamlit](https://streamlit.io)** – Frontend & deployment
- **[Botpress Cloud](https://botpress.com)** – RL Specialist Chatbot
- **HTML/CSS** – Custom styling via `st.markdown`

---

## Contributing

Contributions welcome! Feel free to:
- Open issues
- Submit pull requests
- Suggest UI improvements

---

## License

MIT License – Feel free to use, modify, and distribute.

---

## Author

Mohamed Reda Nkira - Asmae Elhakioui
Engineering Student | IATD-SI  
[GitHub](https://github.com/med-reda-nk) | [LinkedIn](www.linkedin.com/in/mohamed-reda-nkira-5691432a3)

