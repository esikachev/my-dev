import os

from oslo_config import cfg

CONF = cfg.CONF


opts = [
    cfg.StrOpt('host',
               default='http://127.0.0.1:5000',
               help='Url of server with DB'),
    cfg.StrOpt('username',
               help='Username for my_dev')
]

CONF.register_opts(opts)
for location in (os.curdir, os.path.expanduser("~")):
    config = os.path.join(location, ".my.conf")
    if os.path.isfile(config):
        CONF(['--config-file', config])

USER_DOESNT_EXIST = "User with id {} does not exist"
USER_EXIST_MSG = "User exist with {}: {}"
UNABLE_TO_DELETE_USER = "Can not delete user {}: it does't exist"


def list_opts():
    return {'DEFAULT': opts}
