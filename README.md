
---SCREENSHOT---
![AI Resume Reviewer screenshot](https://github.com/saideeraj-929/Ai_Resume_Reviewer/blob/ac91706f168d0021371dcb3dc799cc5526764c6e/Ai_Resume%20screenshot.png)


# 🤖 AI Resume Reviewer

## 📌 Description

**AI Resume Reviewer** is a Python desktop application that uses the **Groq API** and **Llama 3.3 70B Versatile** to analyze resumes and provide professional feedback.

The application allows users to paste their resume, receive an AI-powered review, check the resume word count, save reviews, load previous reviews, and clear the application.

---

## ✨ Features

* 🤖 AI-powered resume review
* 📊 Overall resume score out of 10
* 💪 Strengths analysis
* ⚠️ Weaknesses analysis
* 📝 Grammar and writing feedback
* 💼 Skills identification
* 📋 ATS optimization suggestions
* 💡 Improvement recommendations
* 🔢 Automatic resume word counter
* ⏳ Review status indicator
* 💾 Save AI reviews
* 📂 Load saved reviews
* 🗑️ Clear resume and review
* ⚠️ Error handling
* 🖥️ Simple Tkinter GUI

---

## 🛠️ Technologies Used

* Python 3
* Tkinter
* Groq API
* Llama 3.3 70B Versatile
* File Handling
* Environment Variables
* Exception Handling

---

## 📁 Project Structure

```text
AI-Resume-Reviewer/
│
├── Ai_Review_Resume.py
├── README.md
├── requirements.txt
└── screenshots/
```

---

## 🚀 How It Works

1. Open the application.
2. Paste your resume into the text box.
3. The application automatically counts the words.
4. Click **Review Resume**.
5. The resume is sent to the Groq AI model.
6. AI analyzes the resume.
7. The application displays the review.
8. Users can save or load reviews.

---

## 📊 AI Review Includes

The AI reviewer provides:

### 1. Overall Score

A resume score out of 10.

### 2. Strengths

Identifies the strongest parts of the resume.

### 3. Weaknesses

Identifies areas that need improvement.

### 4. Grammar & Writing

Finds grammar, spelling, and wording problems.

### 5. Skills

Identifies technical and soft skills mentioned in the resume.

### 6. ATS Optimization

Provides suggestions to make the resume more suitable for Applicant Tracking Systems.

### 7. Suggestions

Provides practical recommendations for improving the resume.

### 8. Final Recommendation

Provides a professional summary of what should be improved.

---

## 🔢 Word Counter

The application automatically counts the number of words in the resume.

Example:

```text
Paste resume
     ↓
Words: 245
```

The counter updates while typing.

---

## ⏳ Review Status

The application displays the current review status:

```text
Ready
   ↓
⏳ Reviewing resume...
   ↓
✅ Review completed
```

If an error occurs:

```text
❌ Review failed
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/saideeraj-929/Ai_Resume_Reviewer.git
```

### 2. Open the project

```bash
cd Ai_Resume_Reviewer
```

### 3. Install dependencies

```bash
pip install groq
```

Or:

```bash
pip install -r requirements.txt
```

### 4. Set your Groq API key

**Windows Command Prompt:**

```bash
set GROQ_API_KEY=your_api_key_here
```

**PowerShell:**

```powershell
$env:GROQ_API_KEY="your_api_key_here"
```

### 5. Run the application

```bash
python Ai_Review_Resume.py
```

---

## 📸 Screenshots

Add screenshots of:

* Main application
* Resume word counter
* AI review result

Example:

```text
screenshots/
├── main.png
├── word-counter.png
└── ai-review.png
```

---

## 🎯 Learning Outcomes

This project helped me practice:

* Python programming
* Tkinter GUI development
* Working with AI APIs
* Groq API integration
* Prompt engineering
* Environment variables
* File handling
* Exception handling
* Event handling in Tkinter
* Building practical AI applications
* Improving an existing project instead of creating everything from scratch

---

## 🔮 Future Improvements

* 📄 PDF resume upload
* 📝 DOCX resume upload
* 📊 Resume score visualization
* 🎨 Modern UI
* 📋 Copy review button
* 📥 Export review as PDF
* 🌍 Multiple language support
* 🎯 Job-description matching
* 🔍 ATS keyword matching

---

## 👨‍💻 Author

**Sai Deeraj**

Python Developer | AI/ML Learner | Application Developer

---

## ⭐ Version

**AI Resume Reviewer v2.0**

### Version History

**v1.0**

* Basic AI resume review
* Save/load review
* Clear function
* Tkinter GUI

**v2.0**

* 🔢 Word counter
* ⏳ Review status
* 📊 Improved AI review structure
* 💼 ATS optimization feedback
* 💡 Better resume recommendations

---

## ⭐ Project Status

**Active Development 🚀**
