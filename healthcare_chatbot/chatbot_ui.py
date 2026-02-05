import tkinter as tk
from tkinter import messagebox
import joblib

# Load trained model and vectorizer
model = joblib.load("disease_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_disease():
    user_input = symptom_entry.get("1.0", tk.END).strip()

    if not user_input:
        messagebox.showwarning("Input Error", "Please enter your symptoms")
        return

    input_vector = vectorizer.transform([user_input])
    prediction = model.predict(input_vector)[0]

    result_label.config(
        text=f"🩺 Predicted Disease:\n{prediction}",
        fg="#0a3d62"
    )

# UI window
root = tk.Tk()
root.title("Offline Healthcare Chatbot")
root.geometry("600x450")
root.config(bg="#eaf6f6")

# Heading
tk.Label(
    root,
    text="🩺 Healthcare Chatbot",
    font=("Helvetica", 22, "bold"),
    bg="#eaf6f6",
    fg="#0652DD"
).pack(pady=10)

# Instruction
tk.Label(
    root,
    text="Enter your symptoms (comma separated):",
    font=("Arial", 12),
    bg="#eaf6f6"
).pack()

# Text box
symptom_entry = tk.Text(root, height=6, width=60, font=("Arial", 11))
symptom_entry.pack(pady=10)

# Button
tk.Button(
    root,
    text="Predict Disease",
    font=("Arial", 14, "bold"),
    bg="#1e90ff",
    fg="white",
    padx=20,
    pady=5,
    command=predict_disease
).pack(pady=10)

# Result label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="#eaf6f6"
)
result_label.pack(pady=20)

# Footer
tk.Label(
    root,
    text="⚠️ This is an AI-based prediction, not a medical diagnosis",
    font=("Arial", 9),
    bg="#eaf6f6",
    fg="gray"
).pack(side="bottom", pady=10)

root.mainloop()
