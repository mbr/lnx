def sysfs_lookup(path):
    buf = open(path, 'rb').read()
    if buf and buf[-1] == 0x0A:
        return buf[:-1]
    return buf


def sysfs_lookup_bool(path):
    buf = sysfs_lookup(path)
    if buf == b'0':
        return False
    elif buf == b'1':
        return True
    else:
        raise ValueError('Cannot convert {!r} to bool in {}'.format(buf, path))
