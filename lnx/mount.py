from contextlib import contextmanager
import subprocess


def mount(fst,
          snd=None,
          type=None,
          options=[],
          mount='mount',
          bind=False,
          rbind=False,
          move=False):
    args = ['mount']

    if bind:
        args.append('--bind')
    if rbind:
        args.append('--rbind')
    if move:
        args.append('--move')
    if type is not None:
        args.extend(('-t', type))

    if options:
        args.extend(('-o', ','.join(options)))

    args.append(fst)

    if snd:
        args.append(snd)

    return subprocess.check_call(args)


def umount(target, types=None, force=False, lazy=False, read_only=False):
    args = ['umount']

    if types:
        args.extend(('-t', ','.join(types)))

    if force:
        args.append('-f')

    if read_only:
        args.append('-r')

    if lazy:
        args.append('-l')

    args.append(target)

    return subprocess.check_call(args)


@contextmanager
def mounted(fst, snd=None, *args, **kwargs):
    mount(fst, snd, *args, **kwargs)
    try:
        yield
    finally:
        umount(snd if snd else fst)
