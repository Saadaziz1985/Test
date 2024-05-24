import tkinter as tk
root = tk.Tk()
root.withdraw()
file_path = tk.filedialog.askopenfilename()
print(file_path)
