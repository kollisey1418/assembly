import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
from app_logic import reseption_name, show_drivers

def start_app():
    root = tk.Tk()
    root.title("Driver manage")
    root.geometry("400x400")

    top_frame = tk.Frame(root)
    top_frame.pack(fill="x", pady=5)
    center_frame = tk.Frame(root)
    center_frame.pack(fill="x", pady=15)



    def add_information(top_frame, on_submition):
        def submit():
            first = entry_first.get()
            last = entry_last.get()
            surn = entry_surname.get()
            messagebox.showinfo("Information added", f"{first} {last} {surn}")
            top.destroy()
            on_submition(first, last, surn)

        top = tk.Toplevel(top_frame)
        top.geometry("400x400")
        top.title("Add information")

        tk.Label(top, text="First name:").pack()
        entry_first = tk.Entry(top, width=50)
        entry_first.pack()

        tk.Label(top, text="Last name:").pack()
        entry_last = tk.Entry(top, width=50)
        entry_last.pack()

        tk.Label(top, text="Surname:").pack()
        entry_surname = tk.Entry(top, width=50)
        entry_surname.pack()

        first = entry_first
        last = entry_last
        surn = entry_surname

        tk.Button(top, text="Submit", command=submit).pack()

        return first, last, surn

    tk.Button(top_frame, text="Create a new driver", command=lambda: add_information(top_frame, reseption_name)).pack()



    def select_shift(rows):
            print("Select name: ")
            for idx, row in enumerate(rows, start=1):
                id, first_name, last_name, surname = row
                print(f"{idx}. {first_name}. {last_name}. {surname}")

            choice = int(input("Select driver number: "))
            date_shift = input("Enter driver's date shift: ")
            assignment = input("Select assignment (1/2): ")

            selected_driver = rows[choice - 1]
            id, first_name, last_name, surname = selected_driver
            print(f"{id}. {first_name}. {last_name}. {surname}, {assignment}, {date_shift}")
            return id, assignment, date_shift

    def show_rdirers_ui(parent):
        drivers = show_drivers()
        top = tk.Toplevel(parent)
        top.geometry("400x400")
        top.title("Rdirers")
        for idx, name in enumerate(drivers, start=1):
            tk.Label(top, text=f"{idx}. {name}").pack()



    tk.Button(top_frame, text="Show drivers", command=lambda: show_rdirers_ui(top_frame)).pack()
    root.mainloop()