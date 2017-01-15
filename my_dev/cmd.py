import os


class Cmd(object):
    def ssh_cmd(self, ssh_username, ssh_password, host):
        base_cmd = ('sshpass -p {ssh_password} '
                    '{ssh_username}@{host}'.format(
                        ssh_username=ssh_username,
                        ssh_password=ssh_password,
                        host=host))
        self.run(base_cmd)

    def run(self, cmd):
        os.system(cmd)
