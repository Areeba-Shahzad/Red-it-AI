# Red-it Web Extension

## 📚 Description

Red-it is an innovative web extension meticulously designed to combat information overload by transforming how users interact with online content. It provides intelligent, concise summaries of web pages, making it an indispensable tool for students, researchers, content creators, and professionals who need to quickly grasp the essence of lengthy articles without investing extensive reading time.

Beyond powerful summarization, Red-it offers a comprehensive suite of integrated features, including personalized user experiences through secure login/signup, dynamic flashcard creation for effective memorization, efficient generation of presentation content directly from summaries, a robust history log of all requests, and versatile multi-language support for both summaries and flashcards. This all-in-one tool streamlines information digestion, learning, and content preparation directly within your browser, empowering you to consume and leverage information more effectively.

--- 

<div align="center">
  <img src="Brochure/Brochure_SE_1.png" alt="Red-it Brochure Page 1" width="45%" style="margin-right: 10px;">
  <img src="Brochure/Brochure_SE_2.png" alt="Red-it Brochure Page 2" width="45%">
</div>

---

## 💡 AI Engine

Red-it's core intelligence relies on its **AI Engine**, which uses **OpenAI's GPT-3.5 API (a Large Language Model)**. This AI powers key features:

* **Intelligent Summarization:** It processes web content to provide concise, key-point summaries.
* **Dynamic Flashcard Generation:** The AI analyzes text to create flashcards with questions and answers.
* **Structured Presentation Content:** It transforms summaries into organized outlines suitable for slides.

These functions are based on **Natural Language Processing (NLP)**, with the `interactionwithGPT.py` module managing communication with the OpenAI API for seamless integration.

---

## ✨ Features

* **Intelligent Content Summarization:** Leverage the power of advanced AI (OpenAI's GPT-3.5 API) to distill complex web pages into brief, actionable summaries, providing key insights at a glance.
* **Personalized User Accounts:** Secure login and signup functionality allows users to save preferences, manage their history, and store personalized flashcards and presentation content across sessions.
* **Dynamic Flashcard Generation:** Transform summarized key points into interactive flashcards, customizable with definitions and examples, to aid in memorization and efficient knowledge retention.
* **Effortless Presentation Content Creation:** Convert summaries directly into structured content suitable for presentation slides, dramatically cutting down preparation time for academic or professional briefings.
* **Comprehensive Activity History:** A dedicated history feature logs all summarization, flashcard, and presentation requests, enabling users to easily revisit, manage, and review past interactions.
* **Multi-language Support:** Enhance accessibility and usability with the ability to generate summaries and flashcards in a range of selected languages, catering to a diverse global user base.

---

## 🚀 Installation

To get Red-it up and running in your browser, follow these simple steps:

1.  **Clone the repository:**
    ```bash
    git clone [repository-url]
    cd Red-it/frontend # Navigate into the frontend directory
    ```
2.  **Install Frontend Dependencies & Build:**
    Ensure you have [Node.js](https://nodejs.org/en/download/) and npm/yarn installed.
    ```bash
    npm install
    npm run build # or yarn build. This creates the 'build' folder.
    ```
3.  **Install Backend Dependencies:**
    Navigate to the backend directory and install Python dependencies.
    ```bash
    cd ../backend # Navigate to the backend directory
    pip install -r requirements.txt
    ```
4.  **Start the Backend Server:**
    ```bash
    python server.py # Or use uvicorn for production: uvicorn server:app --host 0.0.0.0 --port 8000
    ```
5.  **Load the Extension in your Browser:**
    * **For Chrome:**
        1.  Open your browser and navigate to `chrome://extensions`.
        2.  Enable "Developer mode" in the top-right corner.
        3.  Click "Load unpacked" and select the `build` folder located within your `frontend` directory (e.g., `Red-it/frontend/build`).
    * **For Firefox:**
        1.  Open your browser and navigate to `about:addons`.
        2.  Click the gear icon (⚙️) and select "Debug Add-ons".
        3.  Click "Load Temporary Add-on..." and select any file inside your `build` folder (e.g., `manifest.json`).

The Red-it extension should now be installed and visible in your browser's extension toolbar.

---

## 📖 Usage

### Summarizing Content

1.  Navigate to any article or web page you wish to summarize.
2.  Click on the **Red-it extension icon** (often looks like an "R" or a small document icon) in your browser's toolbar.
3.  From the popup menu, select the **"Summarize"** option.
4.  The extension will then intelligently process the content of the active page and display a concise, simplified summary directly in the popup, allowing you to quickly grasp the essential information.

### Login/Signup for Personalized Experience

1.  Click on the **Red-it extension icon** in your browser's toolbar.
2.  Choose the **"Login/Signup"** option from the menu.
3.  You will be presented with an interface to either enter your existing credentials to **log in** or complete a quick registration form to **create a new account**. Logging in unlocks personalized features like history tracking and saved content.

### Using the Dashboard

Once logged in, the **Dashboard** acts as your central hub for all Red-it's powerful features:

1.  Click on the **Red-it extension icon** and navigate to the Dashboard.
2.  From here, you can access dedicated buttons for:
    * **Summarization:** Quickly summarize the current page.
    * **Flashcards:** Generate and manage your study flashcards.
    * **Presentation Content:** Create content ready for your slides.
    * **History:** Review your past interactions.
3.  Simply click on the respective button and allow the extension to perform its magic.

### Creating Flashcards

1.  After summarizing content (or from your history), look for the **"Create Flashcard"** option, often available in the summary view or dashboard.
2.  A user-friendly interface will appear, allowing you to easily select key points from the summarized content and customize them into question-and-answer format flashcards.
3.  You can add additional notes or context. Once satisfied, **save the flashcard** to your account for future review.

### Accessing History

1.  From the Dashboard, select the **"History"** option.
2.  This feature provides a chronological log of all your past summarization requests, generated flashcards, and presentation content.
3.  You can easily view, manage, and revisit any past entry, ensuring you always have access to previously processed information.

### Generating Presentation Content

1.  When viewing a summary (or selecting an entry from your history), choose the **"Generate Presentation"** option.
2.  Red-it will transform the key points into structured content, formatted for easy transfer to presentation slides (e.g., bullet points, main headings).
3.  This dramatically speeds up the process of preparing talks, lectures, or reports based on web content.

---

## 🖥️ Tech Stack

- **Frontend**: React.js
- **Backend**: FastAPI (Python 3.9+)
- **Database**: MongoDB
- **AI Integration**: OpenAI GPT-3.5
- **Languages**: English + multilingual translation support

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

### ⚙️ Backend (FastAPI + MongoDB)

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
