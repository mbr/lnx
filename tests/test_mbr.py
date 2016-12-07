from lnx.mbr import CHSAddress

# source: https://en.wikipedia.org/wiki/Logical_block_addressing
LBA_CHS_REF = [(0, (0, 0, 1)),
               (1, (0, 0, 2)),
               (2, (0, 0, 3)),
               (62, (0, 0, 63)),
               (63, (0, 1, 1)),
               (945, (0, 15, 1)),
               (1007, (0, 15, 63)),
               (1008, (1, 0, 1)),
               (1070, (1, 0, 63)),
               (1071, (1, 1, 1)),
               (1133, (1, 1, 63)),
               (1134, (1, 2, 1)),
               (2015, (1, 15, 63)),
               (2016, (2, 0, 1)),
               (16127, (15, 15, 63)),
               (16128, (16, 0, 1)),
               (32255, (31, 15, 63)),
               (32256, (32, 0, 1)),
               (16450559, (16319, 15, 63)),
               (16514063, (16382, 15, 63)), ]


def test_chs_to_lba():
    for lba, (c, h, s) in LBA_CHS_REF:
        chs = CHSAddress(c, h, s)
        assert chs.to_lba() == lba


def test_lba_to_chs():
    for lba, (c, h, s) in LBA_CHS_REF:
        chs = CHSAddress.from_lba(lba)

        assert chs.c == c
        assert chs.h == h
        assert chs.s == s
