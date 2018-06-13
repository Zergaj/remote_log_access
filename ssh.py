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
        time.sleep(5)
        raw_path = stdout.read()
        clean_path = str(raw_path).lstrip("b'").rstrip(r"\n'")
        print('Found file: {}'.format(clean_path), end='\n')
        return clean_path

    def read_logfile(self, path):
        sftp_client = self.client.open_sftp()
        with sftp_client.open(path) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                yield line
