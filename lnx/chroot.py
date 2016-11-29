from contextlib import contextmanager
import os

from .mount import mount, umount


def setup_chroot(chroot, proc=True, sys='/sys', dev='/dev'):
    if proc:
        mount('proc', target=os.path.join(chroot, 'proc'), type='proc')
    if sys:
        mount(sys, os.path.join(chroot, 'sys'), rbind=True)
    if dev:
        mount(dev, os.path.join(chroot, 'dev'), rbind=True)


def deconfigure_chroot(chroot, proc=True, sys=True, dev=True):
    if proc:
        umount(os.path.join(chroot, 'proc'))
    if sys:
        umount(os.path.join(chroot, 'sys'))
    if dev:
        umount(os.path.join(chroot, 'dev'))


@contextmanager
def chroot_binds(chroot, proc='/proc', sys='/sys', dev='/dev'):
    setup_chroot(chroot, proc, sys, dev)
    yield
    deconfigure_chroot(chroot, proc, sys, dev)
