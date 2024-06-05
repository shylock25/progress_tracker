import tkinter as tk
from tkinter import messagebox

class ProgressTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Progress Tracker")
        
        self.tasks = [
            "100 pushups", "100 pullups", "100 situps", 
            "5km run", "3 chapters revision", "2 chapters complete", 
            "30 sums", "15 JEE physics questions", "15 JEE maths questions"
        ]
        
        self.task_vars = [tk.IntVar() for _ in self.tasks]
        self.level = 1
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Daily Tasks", font=("Helvetica", 16)).pack(pady=10)
        
        for idx, task in enumerate(self.tasks):
            tk.Checkbutton(self.root, text=task, variable=self.task_vars[idx]).pack(anchor="w")

        self.level_label = tk.Label(self.root, text=f"Level: {self.level}", font=("Helvetica", 14))
        self.level_label.pack(pady=10)

        tk.Button(self.root, text="Submit", command=self.check_tasks).pack(pady=20)

    def check_tasks(self):
        if all(var.get() for var in self.task_vars):
            self.level += 1
            self.level_label.config(text=f"Level: {self.level}")
            messagebox.showinfo("Congratulations!", "All tasks completed! Level up!")
        else:
            messagebox.showwarning("Incomplete", "Please complete all tasks.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgressTracker(root)
    root.mainloop()
