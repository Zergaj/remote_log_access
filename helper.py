def auth_data(ip):
    data = {
        'ip': ('username', 'password')
    }
    return data[ip]


def auth_data_alt(host):
    usr = input("Enter username to access {}: ".format(host)).strip()
    pwd = input("Enter password for {}: ".format(usr)).strip()
    return usr, pwd


def find_result(log, num_id):
    # Searching num_id in log file.
    # For our goals we need 100 rows before row with num_id and 100 rows after it.
    # To achieve this we store rows in the res list from the first.
    # When lenth of res reaches 100 items, and not found num_id, delete the first item.
    # When num_id is found, add to list another 100 rows and return list.
    # If we reached bottom of list and num_id wasn't found - return empty list.

    res = []
    found_row = False
    num_id_line_index = 0

    for line in log:
        if not found_row:
            if num_id in line:
                found_row = True
                num_id_line_index = len(res)
            if len(res) == 100 and not found_row:
                res = res[1:]
        else:
            if len(res) - num_id_line_index > 100:
                break
        res.append(line)

    if not found_row:
        res = []
    return res


def print_log(result):
    if len(result) == 0:
        print("Num_id wasn't found in log file. Check log_file, maybe it is empty.")
        return

    for i in result:
        print(i, end='')
