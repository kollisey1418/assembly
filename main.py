from db import get_connection
from db_repo import insert_driver, insert_shift
from ui import add_information, select_shift, action_selection
from db_search import search_driver, search_driver_with_shifts


def choice_selection(choice):
    if choice == 1:
        reseption_name()
    elif choice == 2:
        signment_shifts()
    elif choice == 3:
        show_drivers()
    elif choice == 4:
        show_drivers_with_shifts()
    else:
        print("Invalid choice")

def reseption_name():
    conn = get_connection()
    cur = conn.cursor()
    try:
        first, last, surn = add_information()
        insert_driver(cur, first, last, surn)
        conn.commit()
    finally:
        cur.close()
        conn.close()

def signment_shifts():
    conn = get_connection()
    cur = conn.cursor()
    try:
        rows = search_driver(cur)
        driver_id, assignment, date_shift = select_shift(rows)
        insert_shift(cur, driver_id, date_shift, assignment)
        conn.commit()
        print("Result: ", driver_id, assignment, date_shift)
    finally:
        cur.close()
        conn.close()

def show_drivers():
    conn = get_connection()
    cur = conn.cursor()
    try:
        rows = search_driver(cur)

        print("This is all drivers: ")
        print("id_drivers   |   First name        |     Last name        |      Surname")
        for row in rows:
            driver_id, first_name, last_name, surname = row
            print(f"    {driver_id}_______|________{first_name}_________|___________{last_name}___________|___________{surname}")
    finally:
            cur.close()
            conn.close()


def show_drivers_with_shifts():
    conn = get_connection()
    cur = conn.cursor()
    try:
        rows = search_driver_with_shifts(cur)
        print("This is all drivers: ")
        print("id_drivers   |   First name        |     Last name        |      Surname         |           Shifts")
        for row in rows:
            driver_id, first_name, last_name, surname, date, shifts = row
            print(f"    {driver_id}_______|________{first_name}_________|_________{last_name}________|________{surname}________|______{date}______|______{shifts}")
    finally:
        cur.close()
        conn.close()



if __name__ == "__main__":
    while True:
        choice = action_selection()
        choice_selection(choice)
