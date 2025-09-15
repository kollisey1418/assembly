import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog

root = tk.Tk()
root.title("Driver manage")
root.geometry("400x400")



def action_selection():
    label = tk.Label(root, text="You can choose 1 from 3 functions:\n"
                                "1 - Creat a new driver\n"
                                "2 - Select a shift for a driver\n"
                                "3 - Show list of drivers\n"
                                "4 - Show list of drivers with shifts")
    label.pack()




def add_information():
    first = simpledialog.askstring("Name", "Enter driver's first name: ")
    last = simpledialog.askstring("Last name", "Enter driver's last name: ")
    surn = simpledialog.askstring("Surname", "Enter driver's surname: ")
    messagebox.showinfo(f"Driver added:", "{first} {last} {surn}")
    return first, last, surn

action_selection()

btn = tk.Button(root, text="Create a new driver", command=add_information)
btn.pack(pady=10)
root.mainloop()


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

