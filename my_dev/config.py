import os

from oslo_config import cfg

CONF = cfg.CONF


opts = [
    cfg.StrOpt('host',
               default='http://localhost:5000',
               help='Url of server with DB'),
    cfg.StrOpt('username',
               help='Username for my_dev')
]

CONF.register_opts(opts)
for location in (os.curdir, os.path.expanduser("~")):
    config = os.path.join(location, ".my.conf")
    if os.path.isfile(config):
        CONF(['--config-file', '/Users/esikachev/.my.conf'])

USER_DOESNT_EXIST = "User with id {} does not exist"
USER_EXISTS = "User exist with {}: {}"


def list_opts():
    return {'DEFAULT': opts}
