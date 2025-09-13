def insert_driver(cur, first, last, surn):
    cur.execute("INSERT INTO drivers (first_name, last_name, surname) VALUES (%s, %s, %s)", (first, last, surn))


def insert_shift(cur, id, date_shift, assignment):
    cur.execute("INSERT INTO shifts (date, drivers_id, shifts) VALUES (%s, %s, %s)", (date_shift, id, assignment))