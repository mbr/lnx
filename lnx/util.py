import subprocess
import os


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


def sysfs_lookup_int(path):
    buf = sysfs_lookup(path)
    return int(buf.decode('ascii'))


def exit_shell(shell='/bin/bash'):
    if not os.path.exists(shell):
        return False

    return os.execvp(shell, [shell])


def spawn_shell(shell='/bin/bash'):
    if not os.path.exists(shell):
        return False

    proc = subprocess.Popen([shell])
    proc.wait()
