from collections import OrderedDict


class MountInfo(object):
    PROC_INFO = '/proc/self/mountinfo'

    def __init__(self, line):
        fields = line.split(' ')
        self.mount_id = int(fields[0])
        self.parent_id = int(fields[1])
        major, minor = fields[2].split(':', 1)
        self.major = int(major)
        self.minor = int(minor)
        self.root = fields[3]
        self.mount_point = fields[4]
        self.options = fields[5].split(',')

        fields = fields[6:]

        self.optfields = OrderedDict()
        field = fields.pop(0)
        while field != '-':
            k, v = field.split(':', 1)
            self.optfields[k] = v
            field = fields.pop(0)

        self.fstype = fields[0]
        self.source = fields[1]
        self.super_options = fields[2].split(',')

    @classmethod
    def iter_mountinfos(cls):
        for line in open(cls.PROC_INFO):
            yield cls(line)

    def __str__(self):
        return 'MountInfo<{!r} on {!r}>'.format(self.source, self.mount_point)
