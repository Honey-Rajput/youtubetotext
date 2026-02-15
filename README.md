# 🎬 VideoInsight AI — Video Summarizer

Transform any YouTube video into a structured, downloadable summary powered by AI.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ✨ Features

- **Smart Transcript Extraction** — Automatically pulls captions from YouTube videos
- **AI-Powered Summaries** — Choose Brief, Standard, or Detailed summaries
- **Word Document Export** — Download summaries as `.docx` files
- **Text Export** — Download as plain `.txt` files
- **Chat with Video** — Ask follow-up questions about the video content
- **Video Info Panel** — Thumbnail, title, channel, and stats at a glance
- **Premium Dark UI** — Glassmorphism design with smooth animations

## 🚀 Quick Start (Local)

1. **Clone the repo**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Readyoutubevideo.git
   cd Readyoutubevideo
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**

   Create a `.env` file in the project root:
   ```
   EURI_API_KEY=your_euri_api_key_here
   EURI_URL=https://api.euron.one/api/v1/euri/chat/completions
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

## ☁️ Deploy to Streamlit Cloud (Free)

1. Push this repo to **GitHub** (public repo for free hosting)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app** → Select your repo → Set main file to `app.py`
4. Go to **Advanced settings** → **Secrets** and add:
   ```toml
   EURI_API_KEY = "your_euri_api_key_here"
   EURI_URL = "https://api.euron.one/api/v1/euri/chat/completions"
   ```
5. Click **Deploy** — your app will be live in seconds!

## 📋 Requirements

- Python 3.9+
- YouTube videos must have captions (auto-generated or manual)
- EURI API key for AI summarization

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| AI Engine | EURI API (GPT-4.1-nano) |
| Transcripts | youtube-transcript-api |
| Word Export | python-docx |

## 📄 License

MIT License — feel free to use, modify, and share!
