import tkinter as tk
from tkinter import filedialog
import pandas as pd

def merge_files():
    file1 = filedialog.askopenfilename(title="Select first Excel file", filetypes=[("Excel files", "*.xlsx *.xls")])
    if not file1:
        return

    file2 = filedialog.askopenfilename(title="Select second Excel file", filetypes=[("Excel files", "*.xlsx *.xls")])
    if not file2:
        return

    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    merged_df = pd.concat([df1, df2], ignore_index=True)

    output_file = filedialog.asksaveasfilename(title="Save merged Excel file", defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if output_file:
        merged_df.to_excel(output_file, index=False)
        print("Files merged successfully!")

root = tk.Tk()
root.title("Excel Merger")
button = tk.Button(root, text="Merge Excel Files", command=merge_files)
button.pack(pady=20)
root.mainloop()