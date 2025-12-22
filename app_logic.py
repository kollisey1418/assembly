from db import get_connection
from db_repo import insert_driver, insert_shift
from db_search import search_driver_with_shifts, search_driver




def reseption_name(first, last, surn):
    conn = get_connection()
    cur = conn.cursor()
    try:
        insert_driver(cur, first, last, surn)
        conn.commit()
    finally:
        cur.close()
        conn.close()



def show_drivers():
    conn = get_connection()
    cur = conn.cursor()
    try:
        rows = search_driver(cur)
        name = [f"{first} {last} {surn}" for __, first, last, surn in rows]
        return name
    finally:
            cur.close()
            conn.close()


def save_shift(driver_str, shift_value, date_date):
    try:
        first_name, last_name, surname= driver_str.split()
    except ValueError:
        print(f"Driver name {driver_str.split()} is invalid")
        return
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "select id from drivers where first_name = %s AND last_name = %s AND surname = %s",
            (first_name, last_name, surname)
        )
        result = cur.fetchone()
        if result is None:
            print("Driver's ID not found")
        driver_id = result[0]

        cur.execute(
            "INSERT INTO shifts (drivers_id, shifts, date) VALUES (%s, %s, %s)", 
            (driver_id, shift_value, date_date)
        )
        conn.commit()
        print("Driver's shift is save")
    finally:
        cur.close
        conn.close

