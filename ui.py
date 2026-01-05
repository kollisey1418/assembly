import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog, Text
from app_logic import reseption_name, show_drivers, save_shift, show_schedule
from tkcalendar import Calendar
from info_wind import sh_info
import datetime



def start_app():
    root = tk.Tk()
    root.title("Driver manage")
    root.geometry("400x400")

    top_frame = tk.Frame(root)
    top_frame.pack(fill="x", pady=5)
    center_frame = tk.Frame(root)
    center_frame.pack(fill="x", pady=15)
    footer_frame = tk.Frame(root)
    footer_frame.pack(fill="x", pady=15)



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



    #def select_shift(footer_frame):
     #   drivers = show_drivers()
      #  ttk.Label(footer_frame, text="Drivers:").pack()
       # combo = ttk.Combobox(footer_frame)
        #combo['values'] = drivers
        #combo
        #combo.pack()


    def show_rdirers_ui(parent):
        drivers = show_drivers()
        top = tk.Toplevel(parent)
        top.geometry("400x400")
        top.title("Drivers")
        for idx, name in enumerate(drivers, start=1):
            tk.Label(top, text=f"{idx}. {name}").pack()

    def show_schedule_ui(parent):
        schedule = show_schedule()
        top = tk.Toplevel(parent)
        top.geometry("")
        top.title("Schedule")
        

        table = ttk.Treeview(top, columns = ('first', 'last', 'date', 'shifts', 'route'), show = 'headings')
        table.heading('first', text='First Name')
        table.heading('last', text = 'Surname')
        table.heading('date', text = 'Date')
        table.heading('shifts', text = 'Shift')
        table.heading('route', text = 'Route')
        table.pack()
        print(schedule)
        for first, last, shifts, date, route in schedule:
            table.insert(parent = '', index = 0, values = (f'{first} {last} {date} {shifts} {route}'))
        
            



    tk.Button(top_frame, text="Show drivers", command=lambda: show_rdirers_ui(top_frame)).pack()
    tk.Button(top_frame, text="Shift assignment", command=lambda: AssingShift(top_frame)).pack()
    tk.Button(top_frame, text="Show schedule", command=lambda: show_schedule_ui(top_frame)).pack()
    root.mainloop()

class AssingShift:
    def __init__(self, master):
        self.master = master
        self.new_window = tk.Toplevel(master)
        self.new_window.title("Assing Shift")
        self.new_window.geometry("")
        self.lable = tk.Label(self.new_window, text="Shifts")
        self.select_shift()
        self.lable.pack()
        print("Function start")



    def select_shift(self):
        drivers = show_drivers()
        shifts = [1,2,3]
        route = ["Sveti Stefan", "Petrovac", "Lastva", "Braichi", "School-1", "School-2"]

        ttk.Label(self.new_window, text="Drivers:").pack()
        self.combo = ttk.Combobox(self.new_window)
        self.combo['values'] = drivers
        self.combo.pack()

        ttk.Label(self.new_window, text="Shifts:").pack()
        self.combo2 = ttk.Combobox(self.new_window)
        self.combo2['values'] = shifts
        self.combo2.pack()

        ttk.Label(self.new_window, text="Route line").pack()
        self.combo3 = ttk.Combobox(self.new_window)
        self.combo3['values'] = route
        self.combo3.pack()

        date_frame = tk.Frame(self.new_window)
        date_frame.pack()

        self.T = tk.Text(date_frame, height =1, width = 10)
        self.T.insert(tk.END, "select_date")
        self.T.pack(side="right")
        self.data_buton = tk.Button(date_frame, text="Date", command=self.date_selection)
        self.data_buton.pack(side="right")
        tk.Button(self.new_window, text="Save", command=self.submit).pack()


    def date_selection(self):
        today = datetime.date.today()
        self.cal = Calendar(self.new_window, selectmode = 'day',
                    year=today.year,
                    month=today.month,
                    day=today.day)
        self.cal.pack(pady=20)
        self.new_window.update_idletasks()
        self.cal.bind("<<CalendarSelected>>", self.on_select)

    def on_select(self, event):
        raw_date = event.widget.get_date()
        date = datetime.datetime.strptime(raw_date, "%m/%d/%y").strftime("%Y-%m-%d")
        self.T.delete("1.0", tk.END)
        self.T.insert(tk.END, date)
        self.cal.destroy()

    def submit(self):
        driver = self.combo.get()
        shift = self.combo2.get()
        route = self.combo3.get()
        date = self.T.get("1.0", tk.END).strip()
        if date == "select_date":
            print("Date wasn't select")
            sh_info(message='''
            Date wasn't selected!
            Please select date!    
            ''')
            return
        save_shift(driver, shift, route, date)
        info_window_ok(self.new_window)
        print("Function ended")

def info_window_ok(parent):
    info = tk.Toplevel()
    info.title("Confirm proces")
    info.geometry("250x100")
    tk.Label(info, text="oK", font=("Arail", 20)).pack(pady=20)
    info.after(1000, lambda: (info.destroy(),
    parent.destroy()))
    print("Function called")

