import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if height <= 0 or height > 3:  
            messagebox.showerror("Error", "Please enter a valid height (0.1m to 3m).")
            return
        if weight <= 0 or weight > 300: 
            messagebox.showerror("Error", "Please enter a valid weight (1kg to 300kg).")
            return

        bmi = weight / (height ** 2)
        bmi_result = "Your BMI is {:.1f}.\n".format(bmi)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=bmi_result + "Category: " + category)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for height and weight.")

root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Height (m):").grid(row=0, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
