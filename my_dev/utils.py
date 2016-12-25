import os


def write_to_config(username, host):
    with open(os.path.join(os.path.expanduser("~"), '.my.conf'), 'w') as cfg:
        config = '[DEFAULT]\nusername=%s\nhost=%s\n'
        cfg.write(config % (username, host))
