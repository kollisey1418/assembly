import tkinter as tk
from tkinter import ttk

def sh_info(message, title="info"):
    info = tk.Toplevel()
    info.title(title)
    info.geometry("")
    tk.Label(info, text=message, justify="center").pack(pady=10)
    tk.Button(info, text="Ok", command=info.destroy).pack(pady=5)
    info.transient()
    info.focus_set()
    info.grab_set()
