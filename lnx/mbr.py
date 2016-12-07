from struct import unpack


class CHSAddress(object):
    def __init__(self, c, h, s):
        self.c = c
        self.h = h
        self.s = s

    @classmethod
    def from_raw(cls, buf):
        if len(buf) != 3:
            raise ValueError('Raw CHS must be 3 bytes')

        h = buf[0]
        s = buf[1] & 0b00111111
        c = buf[2] | ((buf[1] & 0b11000000) << 2)

        return cls(c, h, s)

    def to_lba(self, hpc=16, spt=63):
        return (self.c * hpc + self.h) * spt + (self.s - 1)

    @classmethod
    def from_lba(cls, lba, hpc=16, spt=63):
        c = lba // (hpc * spt)
        h = (lba // spt) % hpc
        s = (lba % spt) + 1
        return cls(c, h, s)

    def __str__(self):
        return '<CHS {}, {}, {} [LBA: {}]>'.format(self.c, self.h, self.s,
                                                   self.to_lba())


class ParttableEntry(object):
    def __init__(self):
        self._status = 0
        self._first_sect = CHSAddress(0, 0, 0)
        self._part_type = 0
        self._last_sect = CHSAddress(0, 0, 0)
        self._lba = None
        self._length = 0

    @classmethod
    def from_raw(cls, buf, byte_order='<'):
        if len(buf) != 16:
            raise ValueError('Partition table entry must be exactly 16 bytes')

        entry = cls()

        if buf[0] not in (0x00, 0x80):
            raise ValueError('First byte must be one of 0x00, 0x80')

        entry._first_sect = CHSAddress.from_raw(buf[1:4])
        entry._part_type = buf[4]
        entry._last_sect = CHSAddress.from_raw(buf[5:8])
        entry._lba = unpack(byte_order + 'L', buf[8:12])[0]
        entry._length = unpack(byte_order + 'L', buf[12:16])[0]

        return entry
