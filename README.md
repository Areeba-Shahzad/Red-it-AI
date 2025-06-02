# 🧠 Red-it-AI: Your Smart Browsing Companion

**Red-it** is a Chrome extension that enhances your web experience by summarizing pages, creating flashcards, generating presentation content, and tracking your history — all powered by OpenAI GPT-3.5. Designed for students, researchers, and knowledge seekers, Red-it makes absorbing and retaining online content faster and smarter.

---

## ✨ Features

-  **AI Summarization** — Quickly digest the key points of any webpage
-  **Flashcard Generation** — Turn summaries into study-ready flashcards
-  **History Log** — View and manage previous summaries and flashcards
-  **Presentation Creator** — Transform content into ready-made presentation slides
-  **Multi-language Support** — Summaries and flashcards in your preferred language
-  **User Authentication** — Sign up and log in for a personalized experience

---

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/red-it-extension.git

2. Open your browser's extensions page:
   - **Chrome**: `chrome://extensions`
   - **Firefox**: `about:addons`

3. Enable **Developer Mode**

4. Click **Load Unpacked** and select the `/frontend/build` folder

5. Red-it will now be available in your browser’s toolbar

---

## 🧪 Usage Guide

### ✅ Summarize a Page
- Click the Red-it icon
- Select **"Summarize"**
- A simplified summary will be generated using GPT-3.5

### 🧑‍💼 Login/Signup
- Click **Login/Signup** in the popup
- Create an account or log in to access personalized features

### 📌 Create Flashcards
- After summarizing, click **"Create Flashcard"**
- Customize and save flashcards for later review

### 🎤 Generate Presentations
- Use the **"Presentation"** button to convert summaries into structured slides

### 🕹️ Dashboard Access
- The dashboard provides full access to summaries, flashcards, presentation content, and history

---

## 🧱 Project Structure

### 🔧 Frontend (React)

| File             | Description                                |
|------------------|--------------------------------------------|
| `Summary.jsx`     | Summarizes current webpage content         |
| `LoginSignup.jsx` | Handles user login and signup              |
| `Flashcards.jsx`  | UI for creating and reviewing flashcards   |
| `Popup.jsx`       | Main popup interface for extension         |
| `Presentation.jsx`| Generates presentation-ready content       |
| `History.jsx`     | Logs and displays past activity            |
| `Dashboard.jsx`   | Main hub for accessing all features        |

---

### 🧠 Backend (FastAPI + MongoDB)

| File                    | Role                                           |
|-------------------------|------------------------------------------------|
| `server.py`             | Entry point for FastAPI backend                |
| `interactionwithGPT.py`| Handles GPT-3.5 API requests                    |
| `database.py`           | MongoDB operations                             |
| `model.py`              | Pydantic models for data validation            |
| `email_verify.py`       | Verifies the authenticity of signup emails     |
| `name_validation.py`    | Cleans and validates user input                |
| `translator.py`         | Translates content into multiple languages     |
| `webscraping.py`        | Extracts main content from webpages            |
| `testing.js`            | Test suite for backend functionality           |
| `requirements.txt`      | Python dependencies                            |

---

## 🧠 Tech Stack

- **Frontend**: React.js
- **Backend**: FastAPI (Python 3.9+)
- **Database**: MongoDB
- **AI Integration**: OpenAI GPT-3.5
- **Languages**: English + multilingual translation support

---

## 🙌 Acknowledgments

- [OpenAI](https://openai.com/) for GPT-3.5 API  
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)  

