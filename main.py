from ssh import SSH
from helper import *


if __name__ == '__main__':

    ip = input("Enter ip: ").strip()
    mask = input("Enter mask: ").strip()
    row_id = input("Enter row id: ").strip()

    # Store credentials in 'auth_data' and script won't ask you about them.
    # login, password = auth_data(ip)
    login, password = auth_data_alt(ip)

    with SSH(ip, login, password) as ssh:
        path = ssh.path_to_logfile(mask)
        file = ssh.read_logfile(path)
        rows = find_result(file, row_id)
        print_log(rows)
