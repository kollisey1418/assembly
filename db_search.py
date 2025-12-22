def search_driver(cur):
    cur.execute("SELECT * FROM drivers")
    rows = cur.fetchall()
    return rows


def search_driver_with_shifts(cur):
    cur.execute("SELECT drivers.*, shifts.date, shifts.shifts FROM drivers JOIN shifts ON drivers.id = shifts.drivers_id")
    rows = cur.fetchall()
    return rows