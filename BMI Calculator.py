import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

def init_db():
    conn = sqlite3.connect("bmi_data.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bmi_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT,
        weight REAL,
        height REAL,
        bmi REAL,
        category TEXT,
        date TEXT
    )
    """)
    conn.commit()
    conn.close()


def calculate_bmi(weight, height):
    return weight / ((height/100) ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def saveRecord(name, weight, height, bmi, category):
    conn = sqlite3.connect("bmi_data.db")
    cursor = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("""
    INSERT INTO bmi_records (name, weight, height, bmi, category, date)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, weight, height, bmi, category, date))
    conn.commit()
    conn.close()

def CopyAndSave():
    try:
        name = entry_name.get()
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        label_result.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
        saveRecord(name, weight, height, bmi, category)
        messagebox.showinfo("Success", "BMI record saved successfully!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

def show_history():
    name = entry_name.get()
    conn = sqlite3.connect("bmi_data.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT date, bmi FROM bmi_records WHERE name = ? ORDER BY date
    """, (name,))
    records = cursor.fetchall()
    conn.close()

    if records:
        dates = [record[0] for record in records]
        bmis = [record[1] for record in records]

        plt.plot(dates, bmis, marker='o')
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.title(f"BMI Trend for {name}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        messagebox.showinfo("No Data", "No historical data found for this user.")

def main():
    global entry_name, entry_weight, entry_height, label_result

    root = tk.Tk()
    root.title("BMI Calculator")

    tk.Label(root, text="Name:").grid(row=0, column=0)
    entry_name = tk.Entry(root)
    entry_name.grid(row=0, column=1)

    tk.Label(root, text="Weight (kg):").grid(row=1, column=0)
    entry_weight = tk.Entry(root)
    entry_weight.grid(row=1, column=1)

    tk.Label(root, text="Height (cm):").grid(row=2, column=0)
    entry_height = tk.Entry(root)
    entry_height.grid(row=2, column=1)

    label_result = tk.Label(root, text="BMI: \nCategory:")
    label_result.grid(row=3, column=0, columnspan=2)

    tk.Button(root, text="Calculate & Save BMI", command=CopyAndSave).grid(row=4, column=0, columnspan=2)

    tk.Button(root, text="History and Trends", command=show_history).grid(row=5, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    init_db()
    main()
