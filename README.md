[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Y9iW-vs6)
# 🚀 TwinlyAI
### Team: Team Awesome Kids
> *No More Keyword Matching. Start Semantic Recruiting.*

---

## 👥 Team Details

| Name | Role | Email |
| :--- | :--- | :--- |
| **[Jose]** | Team Lead | [kurianjose005@gmail.com] |

---

## 🎯 Problem Statement
Traditional recruiting relies on keyword matching, often missing candidates with the right semantic experience but wrong phrasing. Candidates struggle to convey their full story through static resumes.
* **Context:** Recruiters and hiring managers spend hours sifting through resumes that don't tell the whole story.
* **Impact:** Qualified candidates are overlooked, and companies miss out on top talent.

## 💡 Solution
**TwinlyAI** creates a "Digital Twin" of your professional persona. By uploading your resume, our AI constructs a knowledgeable chatbot that understands your career history deeply.
1.  **Semantic Understanding:** Uses RAG (Retrieval Augmented Generation) to answer questions about your experience based on meaning, not just keywords.
2.  **Embeddable Widget:** Provides a code snippet to place your AI assistant directly on your personal portfolio website.
3.  **Live Interaction:** Allows recruiters to "chat" with your resume, asking specific questions about your skills and projects.

---

## 🛠 Tech Stack

| Category | Technologies Used |
| :--- | :--- |
| **Frontend** | **Next.js 15**, React 19, **Tailwind CSS v4**, Framer Motion, Radix UI |
| **Backend** | **FastAPI**, Python, Uvicorn |
| **AI / LLM** | **LangChain**, **Groq**, OpenAI API, FAISS (Vector DB) |
| **Database** | **MongoDB** (Motor/PyMongo) |
| **Tools** | Docker, Agora (RTC), Recharts |

---

## 📊 MVP Features
- [x] **Resume Ingestion:** Upload PDF, DOCX, or TXT resumes.
- [x] **AI Digital Twin:** Automatically trains a chatbot on your professional history.
- [x] **Smart Embed:** Copy-paste code snippet to embed the bot anywhere.
- [x] **Semantic Search:** Answers queries like "Tell me about a time you led a team" using RAG.
- [ ] **Voice Interaction:** (Planned) Speak directly to the AI candidate.

---

## 🚀 Getting Started

### Prerequisites
- Node.js (v18+)
- Python (v3.10+)
- MongoDB Instance
- API Keys (OpenAI, Groq)

### 1. Backend Setup
```bash
cd Backend
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```
*The backend runs on `http://localhost:8000`*

### 2. Frontend Setup
```bash
cd Frontend
# Install dependencies
npm install

# Run the development server
npm run dev
```
*The frontend runs on `http://localhost:3000`*

---

## 🔗 Links & Demo
- **🌐 Live Site:** [Link to Vercel Deployment]
- **📂 GitHub Repo:** [Link to Repo]
- **📹 Video Demo:** [Link to Video]

> **Testing Credentials (Mock)**
> * **User:** `demo@twinly.ai`
> * **Pass:** `hackathon2026`

---

### 🏆 Acknowledgements
This project was developed during **TechSprint Hackathon 2026**, organized by **GDG on Campus Galgotias University**.
