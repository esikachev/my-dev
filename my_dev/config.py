import sys

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


def list_opts():
    return {'DEFAULT': opts}


def parse_config():
    CONF(project='my-dev', default_config_files=sys.argv[2:])
