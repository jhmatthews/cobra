#!/usr/bin/python
# -*- coding: utf-8 -*-

# definitions from C

NWAVES = 4100
NDIM = 10
NCOMPS = 10
NPARS = 10
NMODS = 800
LINELEN = 132


# structures from C as py classes

class Model:

    def __init__(
        self,
        name,
        par,
        w,
        f,
        nwaves,
        ):
        self.name = name  # type char
        self.par = par  # type double
        self.w = w  # type double
        self.f = f  # type double
        self.nwaves = nwaves  # type int


class ModSum:

    def __init__(
        self,
        name,
        npars,
        nmods,
        modstart,
        modstop,
        min,
        max,
        nwaves,
        ):
        self.name = name  # type char
        self.npars = npars  # type int
        self.nmods = nmods  # type int
        self.modstart = modstart  # type int
        self.modstop = modstop  # type int
        self.min = min  # type double
        self.max = max  # type double
        self.nwaves = nwaves  # type int


