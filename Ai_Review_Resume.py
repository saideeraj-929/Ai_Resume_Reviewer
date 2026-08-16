import tkinter as tk
import os
from groq import Groq
from tkinter import messagebox
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
window = tk.Tk()
window.title("🤖 AI Resume Reviewer")
window.geometry("700x600")
window.config(bg="#EAF4FF")
REVIEW_FILE="review.txt"
title = tk.Label(
    window,
    text="🤖 AI Resume Reviewer ",
    font=("Arial", 18, "bold"),
    bg="#EAF4FF"
)

title.pack(pady=10)
def save_review():
    review= response_box.get("1.0",tk.END)
    with open(REVIEW_FILE,"w") as file:
        file.write(review)
    messagebox.showinfo(
        "Success",
        "Review saved successfully!"
    )
def load_review():
    try:
        with open(REVIEW_FILE,"r") as file:
            review = file.read()
            response_box.delete("1.0",tk.END)
            response_box.insert(tk.END,review)

        messagebox.showinfo("Success",
            "Review loaded successfully!"
         )
    except FileNotFoundError:
        messagebox.showerror("Error",
            "No saved review found"
                             )
def word_length(event=None):
    resume =resume_entry.get("1.0",tk.END).strip()
    if resume :
        count =len(resume.split())
    else:
        count =0
    word_label.config(text=f"words:{count}")
  

def clear():
    resume_entry.delete("1.0", tk.END)
    response_box.delete("1.0", tk.END)

    if os.path.exists(REVIEW_FILE):
        os.remove(REVIEW_FILE)
def review_resume():
    resume = resume_entry.get("1.0", tk.END).strip()

    if resume == "":
        response_box.delete("1.0", tk.END)
        response_box.insert(tk.END, "Please paste your resume first.")
        return
    status_label.config(text="⏳ Reviewing resume...")
    window.update()
    messages = [
        {
            "role": "system",
            "content": """
            You are an expert HR Resume Reviewer.

            Review the user's resume.

            Give:
            1. Overall score out of 10
            2. Strengths
            3. Weaknesses
            4. Grammar mistakes
            5. Suggestions for improvement
            6. Final recommendation

            Keep your answer professional.
            """
        },
        {
            "role": "user",
            "content": resume
        }
    ]

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
            )
        review=response.choices[0].message.content
        response_box.delete("1.0",tk.END)
        response_box.insert(tk.END,review)
        status_label.config(text="✅ Review completed")
    except Exception as e:
        response_box.delete("1.0", tk.END)
        response_box.insert(tk.END, f"Error:\n\n{e}")
        status_label.config(text="❌ Review failed")
tk.Label(window,text="Paste your Resume here",font=("Arial",13,"bold")).pack()

resume_entry = tk.Text(
    window,

    width=60,
    height=6,
    
)
resume_entry.pack(pady=10)
resume_entry.bind("<KeyRelease>", word_length)
word_label=tk.Label(window,text="Words:0",font=("Arial",11),bg="pink")
word_label.pack(pady=5)
status_label = tk.Label(
    window,
    text="Ready",
    font=("Arial", 10),
    bg="#EAF4FF"
)

status_label.pack(pady=5)

review_button=tk.Button(window,text="Review Resume",font=("Arial",11),bg="#2196F3",command=review_resume)
review_button.pack(pady=5)
save_button=tk.Button(window,text="Save Review",font=("Arial",11),bg="#4CAF50",command=save_review)
save_button.pack(pady=5)
load_button=tk.Button(window,text="Load Review",font=("Arial",11),bg="#FFC107",command=load_review)
load_button.pack(pady=5)
clear_button=tk.Button(window,text="Clear",font=("Arial",11),bg="Red",command=clear)
clear_button.pack(pady=5)
Ai_review_label=tk.Label(window,text="AI Review",font=("Arial",13,"bold")).pack()

response_box = tk.Text(
    window,
    width=70,
    height=15,
    font=("Arial", 11),
    wrap="word"
)
response_box.pack(pady=10)


window.mainloop()
