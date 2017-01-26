def parse_ssh(args):
    ssh_args = args[0].split('@')
    return ssh_args[0], ssh_args[1]
