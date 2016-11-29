import subprocess


def mount(source=None,
          target=None,
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

    if source:
        args.extend(('--source', source))
    if target:
        args.extend(('--target', target))

    if options:
        args.extend(('-o', ','.join(options)))

    return subprocess.check_call(args)


def umount(target, types=None, force=False, read_only=False):
    args = ['umount']

    if types:
        args.extend(('-t', ','.join(types)))

    if force:
        args.append('-f')

    if read_only:
        args.append('-r')

    args.append(target)

    return subprocess.check_call(args)
