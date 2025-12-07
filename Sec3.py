from tkinter import *
from tkinter import messagebox

r = Tk()
r.geometry("400x400")
r.title("Feedback Form")

Label(r, text="Feedback Form", font=("Arial", 18, "bold")).pack(pady=20)

Label(r, text="Your Name:", font=("Arial", 12)).pack()
name = Entry(r, font=("Arial", 12))
name.pack(pady=5)

Label(r, text="Rate Us (1–5):", font=("Arial", 12)).pack()
rating = Entry(r, font=("Arial", 12))
rating.pack(pady=5)

Label(r, text="Comments:", font=("Arial", 12)).pack()
comment = Text(r, width=30, height=4, font=("Arial", 12))
comment.pack(pady=5)

def submit_feedback():
    n = name.get()
    r = rating.get()
    c = comment.get("1.0", "end").strip()

    if n == "" or r == "" or c == "":
        messagebox.showerror("Error", "Fill all fields!")
        return

    if not r.isdigit() or not (1 <= int(r) <= 5):
        messagebox.showerror("Error", "Rating must be between 1 and 5!")
        return

    messagebox.showinfo("Thank You", "Feedback submitted successfully!")

Button(r, text="Submit", command=submit_feedback, bg="purple", fg="white",
       font=("Arial", 12)).pack(pady=20)

r.mainloop()