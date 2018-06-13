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
    res = []
    found_row = False
    id_line_index = 0
    for line in log:
        if not found_row:
            if num_id in line:
                found_row = True
                id_line_index = len(res)
            if len(res) == 100 and not found_row:
                res = res[1:]
        else:
            if len(res) - id_line_index > 100:
                break
        res.append(line)
    return res


def print_log(result):
    for i in result:
        print(i, end='')
