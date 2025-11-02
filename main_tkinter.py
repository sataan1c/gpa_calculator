import tkinter as tk
from tkinter import ttk, messagebox
from subject import Subject


class GPACalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GPA Calculator")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self.subjects = []
        self.total_subjects = 0
        self.current_index = 0

        
        self.frame_count = ttk.Frame(root, padding=20)
        self.frame_count.pack(fill="x")

        ttk.Label(self.frame_count, text="Enter the number of subjects:").pack(pady=5)
        self.entry_count = ttk.Entry(self.frame_count, width=10, justify="center")
        self.entry_count.pack(pady=5)

        ttk.Button(self.frame_count, text="Start Input", command=self.start_input).pack(pady=10)

       
        self.frame_input = ttk.LabelFrame(root, text="Enter Subject Data", padding=15)
        self.label_progress = ttk.Label(self.frame_input, text="")
        self.entry_name = ttk.Entry(self.frame_input, width=25)
        self.entry_pre = ttk.Entry(self.frame_input, width=10)
        self.entry_exam = ttk.Entry(self.frame_input, width=10)

        ttk.Label(self.frame_input, text="Subject Name:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame_input, text="Pre-Exam Points:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_pre.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.frame_input, text="Exam Points:").grid(row=3, column=0, padx=5, pady=5)
        self.entry_exam.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(self.frame_input, text="Next Subject", command=self.add_subject).grid(row=4, column=0, columnspan=2, pady=10)

        
        self.frame_result = ttk.LabelFrame(root, text="Results", padding=10)
        self.table = ttk.Treeview(self.frame_result, columns=("name", "final", "gpa", "grade"), show="headings")
        for col, name in [("name", "Subject"), ("final", "Final"), ("gpa", "GPA"), ("grade", "Grade")]:
            self.table.heading(col, text=name)
            self.table.column(col, anchor="center", width=100)
        self.table.pack(fill="both", expand=True)

        self.avg_label = ttk.Label(root, text="Average GPA: 0.00", font=("Arial", 12, "bold"))
        self.avg_label.pack(pady=10)

    def start_input(self):
        try:
            count = int(self.entry_count.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return

        if count <= 0:
            messagebox.showerror("Error", "Number of subjects must be positive!")
            return

        self.total_subjects = count
        self.current_index = 1
        self.subjects = []

        self.frame_count.pack_forget()  
        self.frame_input.pack(padx=10, pady=10, fill="x")
        self.label_progress.grid(row=0, column=0, columnspan=2, pady=5)
        self.label_progress.config(text=f"Subject {self.current_index} of {self.total_subjects}")

    def add_subject(self):
        name = self.entry_name.get().strip()
        pre = self.entry_pre.get().strip()
        exam = self.entry_exam.get().strip()

        if not name or not pre or not exam:
            messagebox.showwarning("Warning", "Please fill in all fields!")
            return

        try:
            pre = int(pre)
            exam = int(exam)
        except ValueError:
            messagebox.showerror("Error", "Points must be integers!")
            return

        subject = Subject(name, pre, exam)
        self.subjects.append(subject)

        self.entry_name.delete(0, tk.END)
        self.entry_pre.delete(0, tk.END)
        self.entry_exam.delete(0, tk.END)

        if self.current_index < self.total_subjects:
            self.current_index += 1
            self.label_progress.config(text=f"Subject {self.current_index} of {self.total_subjects}")
        else:
            self.show_results()

    def show_results(self):
        self.frame_input.pack_forget()
        self.frame_result.pack(padx=10, pady=10, fill="both", expand=True)

       
        for s in self.subjects:
            self.table.insert("", "end", values=(s.subject_name, s.final_point, s.gpa, s.letter_grade))

       
        avg_gpa = sum(s.gpa for s in self.subjects) / len(self.subjects)
        self.avg_label.config(text=f"Average GPA: {avg_gpa:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GPACalculatorApp(root)
    root.mainloop()
