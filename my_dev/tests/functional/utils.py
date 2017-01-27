from oslo_utils import uuidutils


def rand_name(name=''):
    rand_data = uuidutils.generate_uuid()[:8]
    if name:
        return '%s-%s' % (name, rand_data)
    else:
        return rand_data
