def search_driver(cur):
    cur.execute("SELECT * FROM drivers")
    rows = cur.fetchall()
    return rows


def search_schedule(cur):
    cur.execute('''SELECT drivers.first_name, drivers.last_name, shifts.date, shifts.shifts, shifts.route 
                FROM drivers 
                JOIN shifts ON drivers.id=shifts.drivers_ID''')
    rows = cur.fetchall()
    return rows