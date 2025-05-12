# loan_gui.py
import tkinter as tk
from tkinter import messagebox

def calculate_loan():
    try:
        loan_amount = float(entry_amount.get())
        annual_rate = float(entry_rate.get())
        years = int(entry_years.get())

        monthly_rate = annual_rate / 12 / 100
        months = years * 12

        # Monthly payment formula
        monthly_payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -months)
        total_payment = monthly_payment * months

        # Display formatted output
        result_text = (
            f"Monthly Payment: ${monthly_payment:,.2f}\n"
            f"Total Payment: ${total_payment:,.2f}"
        )
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# GUI Setup
window = tk.Tk()
window.title("Loan Payment Calculator")

tk.Label(window, text="Loan Amount ($):").grid(row=0, column=0, pady=5, padx=5)
entry_amount = tk.Entry(window)
entry_amount.grid(row=0, column=1, pady=5)

tk.Label(window, text="Annual Interest Rate (%):").grid(row=1, column=0, pady=5, padx=5)
entry_rate = tk.Entry(window)
entry_rate.grid(row=1, column=1, pady=5)

tk.Label(window, text="Loan Term (Years):").grid(row=2, column=0, pady=5, padx=5)
entry_years = tk.Entry(window)
entry_years.grid(row=2, column=1, pady=5)

result_label = tk.Label(window, text="Enter loan details to calculate.", fg="blue")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

calculate_button = tk.Button(window, text="Calculate", command=calculate_loan)
calculate_button.grid(row=4, column=0, columnspan=2, pady=5)

window.mainloop()
