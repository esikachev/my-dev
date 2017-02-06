import os


class Cmd(object):
    def ssh_cmd(self, ssh_username, ssh_password, host):
        separator = ''
        if ssh_username:
            separator = '@'
        base_cmd = ('sshpass -p {ssh_password} ssh '
                    '{ssh_username}{separator}{host}'.format(
                            ssh_username=ssh_username,
                            separator=separator,
                            ssh_password=ssh_password,
                            host=host))
        self.run(base_cmd)

    def run(self, cmd):
        os.system(cmd)
