# loan_gui_with_file.py
import tkinter as tk
from tkinter import messagebox

def calculate_and_save():
    try:
        loan_amount = float(entry_amount.get())
        annual_rate = float(entry_rate.get())
        years = int(entry_years.get())

        monthly_rate = annual_rate / 12 / 100
        months = years * 12

        monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -months)
        total_payment = monthly_payment * months

        result = (
            f"Loan: ${loan_amount:,.2f}, Rate: {annual_rate:.2f}%, "
            f"Years: {years}, Monthly: ${monthly_payment:,.2f}, Total: ${total_payment:,.2f}"
        )

        result_label.config(text=result)

        with open("loan_data.txt", "a") as file:
            file.write(result + "\n")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# GUI Setup
window = tk.Tk()
window.title("Loan Calculator + Save to File")

tk.Label(window, text="Loan Amount ($):").grid(row=0, column=0, pady=5, padx=5)
entry_amount = tk.Entry(window)
entry_amount.grid(row=0, column=1)

tk.Label(window, text="Interest Rate (%):").grid(row=1, column=0, pady=5, padx=5)
entry_rate = tk.Entry(window)
entry_rate.grid(row=1, column=1)

tk.Label(window, text="Loan Term (Years):").grid(row=2, column=0, pady=5, padx=5)
entry_years = tk.Entry(window)
entry_years.grid(row=2, column=1)

result_label = tk.Label(window, text="Results will appear here", fg="green")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

save_button = tk.Button(window, text="Calculate & Save", command=calculate_and_save)
save_button.grid(row=4, column=0, columnspan=2, pady=5)

window.mainloop()
