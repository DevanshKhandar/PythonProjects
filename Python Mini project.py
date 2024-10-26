import tkinter as tk
from tkinter import messagebox

# Function to classify the ratio into Very Good, Good, Average, or Bad
def classify_ratio(value, ranges):
    if ranges[0][0] <= value <= ranges[0][1]:
        return "Very Good"
    elif ranges[1][0] <= value <= ranges[1][1]:
        return "Good"
    elif ranges[2][0] <= value <= ranges[2][1]:
        return "Average"
    else:
        return "Bad"

# Function to evaluate the company based on its ratios
def evaluate_company(ratios):
    ratios['PE Comparison'] = ratios['Sector PE'] / ratios['PE Ratio']
    ratios['PB Comparison'] = ratios['Sector PB'] / ratios['PB Ratio']

    classifications = {
        'PE Comparison': [(1.5, float('inf')), (1, 1.5), (1, 1), (0, 1)],
        'PB Comparison': [(1.4, float('inf')), (1.2, 1.4), (1, 1.2), (0, 1)],
        'Quick Ratio': [(1.5, float('inf')), (1, 1.5), (0.8, 1), (0, 0.8)],
        'Current Ratio': [(1.5, float('inf')), (1, 1.5), (0.8, 1), (0, 0.8)],
        'Return on Equity (%)': [(15, float('inf')), (10, 15), (5, 10), (0, 5)],
        'Return on Capital Employed (%)': [(15, float('inf')), (10, 15), (5, 10), (0, 5)],
        'Return on Investment (%)': [(15, float('inf')), (10, 15), (5, 10), (0, 5)],
        'Debt to Equity Ratio': [(0, 2.5), (2.5, 4), (4, float('inf'))],
        '5Y CAGR (%)': [(15, float('inf')), (10, 15), (5, 10), (0, 5)],
        'Interest Coverage Ratio': [(3, float('inf')), (2, 3), (1.5, 2), (0, 1.5)],
        'RSI-14D': [(60, float('inf')), (30, 60), (0, 30)]
    }

    ratings = {'Very Good': 0, 'Good': 0, 'Average': 0, 'Bad': 0}

    for ratio_name, ratio_value in ratios.items():
        if ratio_name in classifications:
            rating = classify_ratio(ratio_value, classifications[ratio_name])
            ratings[rating] += 1

    if ratings['Bad'] > 0:
        return "Company is a Bad Buy based on the financial ratios."
    elif ratings['Very Good'] > ratings['Good'] and ratings['Very Good'] >= ratings['Average']:
        return "Company is a Very Good Buy based on the financial ratios."
    elif ratings['Good'] >= ratings['Average']:
        return "Company is a Good Buy based on the financial ratios."
    else:
        return "Company is an Average Buy based on the financial ratios."

# GUI code to get the financial ratios from the user
def get_ratios_from_gui():
    ratios = {}
    for field in fields:
        try:
            ratios[field] = float(entries[field].get())
        except ValueError:
            messagebox.showerror("Input Error", f"Invalid input for {field}. Please enter a numeric value.")
            return None
    return ratios

# Function to display the evaluation result
def evaluate_company_gui():
    ratios = get_ratios_from_gui()
    if ratios:
        result = evaluate_company(ratios)
        messagebox.showinfo("Final Verdict", result)

# Creating the GUI window
root = tk.Tk()
root.title("Company Evaluation Tool")

fields = [
    "PE Ratio", "Sector PE", "PB Ratio", "Sector PB", "Quick Ratio", 
    "Current Ratio", "Debt to Equity Ratio", "Debt Ratio", "Return on Equity (%)", 
    "Return on Capital Employed (%)", "Return on Investment (%)", "5Y CAGR (%)", 
    "Interest Coverage Ratio", "RSI-14D"
]

entries = {}
for idx, field in enumerate(fields):
    tk.Label(root, text=field).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
    entry = tk.Entry(root)
    entry.grid(row=idx, column=1, padx=10, pady=5)
    entries[field] = entry

# Button to trigger the evaluation
evaluate_button = tk.Button(root, text="Evaluate Company", command=evaluate_company_gui)
evaluate_button.grid(row=len(fields), column=0, columnspan=2, pady=20)

root.mainloop()
