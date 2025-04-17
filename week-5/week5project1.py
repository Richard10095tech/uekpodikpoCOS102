import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Load the dataset
try:
    df = pd.read_csv("GIG-logistics.csv")
except FileNotFoundError:
    print("CSV file not found. Please make sure GIG-logistics.csv is in the same folder.")
    exit()

def verify_employee():
    name = name_entry.get().strip()
    department = dept_entry.get().strip()

    # Search for employee
    match = df[(df['Name'].str.lower() == name.lower()) & 
               (df['Department'].str.lower() == department.lower())]

    if not match.empty:
        # Employee exists
        welcome_window = tk.Toplevel(root)
        welcome_window.title("Welcome")
        welcome_window.geometry("400x200")
        
        msg = f"Welcome {name.title()}!\n\nHere are your colleagues in {department.title()}:"
        tk.Label(welcome_window, text=msg).pack()

        # Display other department members
        colleagues = df[(df['Department'].str.lower() == department.lower()) & 
                        (df['Name'].str.lower() != name.lower())]

        if not colleagues.empty:
            for col in colleagues['Name']:
                tk.Label(welcome_window, text=f"- {col}").pack()
        else:
            tk.Label(welcome_window, text="(You are the only one in this department!)").pack()

    else:
        messagebox.showinfo("Result", "Employee not found. Please check name or department.")

# GUI setup
root = tk.Tk()
root.title("GIG Logistics Employee Verifier")
root.geometry("400x250")

tk.Label(root, text="Enter Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Enter Department:").pack()
dept_entry = tk.Entry(root)
dept_entry.pack()

verify_button = tk.Button(root, text="Verify", command=verify_employee)
verify_button.pack(pady=10)

root.mainloop()
 