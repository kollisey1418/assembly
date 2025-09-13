
def action_selection():
    print('''You can choose 1 from 3 functions
    1 - Creat a new driver
    2 - Select a shift for a driver
    3 - Show list of drivers
    4 - Show list of drivers with shifts''')
    choice = int(input("Select action: "))
    return choice


def add_information():
    first = input("Enter driver's first name: ")
    last = input("Enter driver's last name: ")
    surn = input("Enter driver's surname: ")
    return first, last, surn

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

