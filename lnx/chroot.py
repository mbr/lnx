from contextlib import contextmanager

from .mount import mount, umount


def setup_chroot(chroot, proc='/proc', sys='/sys', dev='/dev'):
    if proc:
        mount(type='proc', source=proc, target=os.path.join(chroot, 'proc'))
    if sys:
        mount(rbind=True, source=sys, target=os.path.join(chroot, 'sys'))
    if dev:
        mount(rbind=True, source=dev, target=os.path.join(chroot, 'dev'))


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
