#!/usr/bin/env python
import os
import Gauss_Legendre_mpmath
import reverse_tan
import reverse_tan_John_Machin
import reverse_tan_Euler
import pi_compare
import unbounded_spigot
import spigot
import Chudnovsky

from os.path import dirname, basename, isfile
import glob

modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f).split('.')[0] for f in modules if isfile(f)]

