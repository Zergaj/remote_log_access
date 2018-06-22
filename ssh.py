import paramiko
import time


class SSH:
    def __init__(self, ip, login, password):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ip = ip
        self.login = login
        self.password = password

    def __enter__(self):
        self.client.connect(hostname=self.ip, username=self.login, password=self.password)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def path_to_logfile(self, mask):
        stdin, stdout, stderr = self.client.exec_command('find / -name "*{}*" 2>/dev/null\n'.format(mask))
        time.sleep(5)               # waiting for command execution. not a good approach, but works for now
        raw_path = stdout.read()
        path_data = str(raw_path).lstrip("b'").rstrip(r"\n'").split(r'\n')
        return self.checker(path_data)

    def read_logfile(self, path):
        sftp_client = self.client.open_sftp()
        try:
            with sftp_client.open(path) as f:
                return f
        except FileNotFoundError:
            return False

    @staticmethod
    def checker(data):
        if len(data) == 1:      # if found only one file - return it
            return data[0]
        elif len(data) > 1:     # if found more then one, ask user what file should be opened
            print('Found files: ')
            for i in data:
                print("id: {0}, path: {1}".format(data.index(i), i))
            path = int(input("To open file enter its id: ").strip())
            return data[path]
        else:                   # else list is empty and file wasn't found
            print('File not found')
            return False
