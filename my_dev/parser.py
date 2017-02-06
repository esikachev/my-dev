def parse_ssh(args):
    ssh_args = args[0].split('@')
    if len(ssh_args) == 1:
        ssh_args.insert(0, '')
    return ssh_args[0], ssh_args[1]
