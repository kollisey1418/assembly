from db import get_connection
from db_search import search_driver
from ui import select_shift
from db_repo import insert_shift

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