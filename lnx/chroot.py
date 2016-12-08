from contextlib import contextmanager
import os

from .mount import mount, umount


def setup_chroot(chroot, proc=True, sys='/sys', dev='/dev'):
    if proc:
        mount('proc', os.path.join(chroot, 'proc'), type='proc')
    if sys:
        mount('sys', os.path.join(chroot, 'sys'), type='sysfs')
    if dev:
        mount(dev, os.path.join(chroot, 'dev'), bind=True)


def teardown_chroot(chroot, proc=True, sys=True, dev=True):
    if dev:
        umount(os.path.join(chroot, 'dev'), lazy=True)
    if sys:
        umount(os.path.join(chroot, 'sys'), lazy=True)
    if proc:
        umount(os.path.join(chroot, 'proc'), lazy=True)


@contextmanager
def chroot_binds(chroot, proc='/proc', sys='/sys', dev='/dev'):
    setup_chroot(chroot, proc, sys, dev)
    try:
        yield
    finally:
        teardown_chroot(chroot, proc, sys, dev)
