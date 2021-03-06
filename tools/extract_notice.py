#!/usr/bin/python
# -*- python -*-
# -*- coding: utf-8 -*-
# vim:filetype=python:
# Extract copyright notice from copyright_notice.txt file
# (c) Roberto Di Remigio  <roberto.d.remigio@uit.no>
# licensed under the GNU Lesser General Public License

import os
import re
import string

def extractor():
    # Read copyright notice from file
    curdir = os.path.dirname(os.path.realpath(__file__))
    with open(curdir+'/copyright_notice.txt', 'r') as myfile:
        notice = myfile.readlines()
    # Form copyright notice comment
    pcmsolver_copyright_fortran = '\n'
    pcmsolver_copyright_c       = '\n/*\n'
    for line in notice:
        line_fortran = '! ' + line
        pcmsolver_copyright_fortran += line_fortran
        line_c       = ' *     ' + line.lstrip(' ')
        pcmsolver_copyright_c       += line_c
    pcmsolver_copyright_c += ' */\n'
    return (pcmsolver_copyright_fortran, pcmsolver_copyright_c)

# vim:et:ts=4:sw=4
