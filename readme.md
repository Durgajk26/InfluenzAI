# InfluenzAI 🎯

![Python](https://img.shields.io/badge/Python-0d0d0d?style=for-the-badge&logo=python&logoColor=FF007F)
![Streamlit](https://img.shields.io/badge/Streamlit-0d0d0d?style=for-the-badge&logo=streamlit&logoColor=FF007F)
![Groq AI](https://img.shields.io/badge/Groq%20AI-0d0d0d?style=for-the-badge&logo=groq&logoColor=FF007F)
![Llama](https://img.shields.io/badge/Llama%203.3-0d0d0d?style=for-the-badge&logo=meta&logoColor=FF007F)

> An AI-powered influencer command centre — track your performance, get smart suggestions, and generate captions with AI.

---

## Features

- **Live metrics dashboard** — followers, engagement rate, reach, and post count at a glance
- **AI suggestions** — smart tips on when to post, what content to create, and hashtag strategy
- **AI caption generator** — pick your niche, platform, and mood → get real captions instantly powered by Llama 3.3 via Groq
- **Clean minimal UI** — built with Streamlit for fast, beautiful rendering

---

## Demo

> Screenshot or GIF coming soon

---

## Getting Started

```bash
git clone https://github.com/Durgajk26/InfluenzAI.git
cd InfluenzAI
pip install -r requirements.txt
```

Create a `.env` file in the root folder:
```
GROQ_API_KEY=your-groq-api-key-here
```

Then run:
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

> Get a free Groq API key at [console.groq.com](https://console.groq.com)

---

## Tech Stack

| Layer | Tool |
|---|---|
| UI Framework | Streamlit |
| AI Engine | Groq API (Llama 3.3 70B) |
| Language | Python 3.10+ |
| Environment | python-dotenv |

---

## Roadmap

- [x] Dashboard with live metrics
- [x] AI suggestion cards
- [x] Caption generator UI
- [x] Connect Groq AI for real caption generation
- [ ] Connect Instagram API for live data
- [ ] Deploy to Streamlit Cloud

---

## Author

**Durga Muthukrishnan** — AI Engineer | MSc Data Science & AI @ Middlesex University Dubai  
[GitHub](https://github.com/Durgajk26) · [LinkedIn](https://linkedin.com/in/durgamuthukrishnan)

---

## License

MIT