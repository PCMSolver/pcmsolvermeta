#!/usr/bin/python
# -*- python -*-
# -*- coding: utf-8 -*-
# vim:filetype=python:
# Update contents of copyright notice on top of source files.
# If no files are given as arguments, the script will glob in the invocation
# directory.
# (c) Roberto Di Remigio  <roberto.d.remigio@uit.no>
# licensed under the GNU Lesser General Public License

import docopt
import os
import re
import string
import sys
from extract_notice import extractor

options = """
Usage:
    ./update_copyright.py [options] [<filenames>]
    ./update_copyright.py (-h | --help)

Options:
  --lang=<LANGUAGE> Programming language of the file <CXX/C/F> [default: CXX].
  <filenames>       List of files.
  -h --help         Show this screen.
"""

def from_file(file):
    f = open(file, 'r')
    s = f.read()
    f.close()
    return s


def to_file(s, file):
    f = open(file, 'w')
    f.write(s)
    f.close()


def update_notice_fortran(file_list):
    # fortran files pcmsolver copyright
    p = re.compile('(?<=' + pcmsolver_copyright_fortran_start + ').*(?=' + pcmsolver_copyright_fortran_end + ')', re.DOTALL)
    for file in file_list:
        s = from_file(file)
        if pcmsolver_copyright_fortran_start in s:
            s = re.sub(p, pcmsolver_copyright_fortran, s)
            to_file(s, file)


def update_notice_c(file_list):
    # c files pcmsolver copyright
    p = re.compile('(?<=' + pcmsolver_copyright_c_start + ').*(?=' + pcmsolver_copyright_c_end + ')', re.DOTALL)
    for file in file_list:
        s = from_file(file)
        if string.replace(pcmsolver_copyright_c_start, '\\', '') in s:
            s = re.sub(p, pcmsolver_copyright_c, s)
            to_file(s, file)


def update_notice_h(file_list):
    # h files pcmsolver copyright
    p = re.compile('(?<=' + pcmsolver_copyright_c_start + ').*(?=' + pcmsolver_copyright_c_end + ')', re.DOTALL)
    for file in file_list:
        s = from_file(file)
        if string.replace(pcmsolver_copyright_c_start, '\\', '') in s:
            s = re.sub(p, pcmsolver_copyright_c, s)
            to_file(s, file)


def update_notice_cpp(file_list):
    # cpp files pcmsolver copyright
    p = re.compile('(?<=' + pcmsolver_copyright_c_start + ').*(?=' + pcmsolver_copyright_c_end + ')', re.DOTALL)
    for file in file_list:
        s = from_file(file)
        if string.replace(pcmsolver_copyright_c_start, '\\', '') in s:
            s = re.sub(p, pcmsolver_copyright_c, s)
            to_file(s, file)


def update_notice_hpp(file_list):
    # hpp files pcmsolver copyright
    p = re.compile('(?<=' + pcmsolver_copyright_c_start + ').*(?=' + pcmsolver_copyright_c_end + ')', re.DOTALL)
    for file in file_list:
        s = from_file(file)
        if string.replace(pcmsolver_copyright_c_start, '\\', '') in s:
            s = re.sub(p, pcmsolver_copyright_c, s)
            to_file(s, file)


try:
    arguments = docopt.docopt(options, argv=None)
except docopt.DocoptExit:
    sys.stderr.write('ERROR: bad input to %s\n' % sys.argv[0])
    sys.stderr.write(options)
    sys.exit(-1)

filenames = arguments['<filenames>']
language  = arguments['--lang']

pcmsolver_copyright_fortran, pcmsolver_copyright_c = extractor()

pcmsolver_copyright_fortran_start = '!pcmsolver_copyright_start'
pcmsolver_copyright_fortran_end   = '!pcmsolver_copyright_end'

pcmsolver_copyright_c_start = '/\* pcmsolver_copyright_start \*/'
pcmsolver_copyright_c_end   = '/\* pcmsolver_copyright_end \*/'

fortran_file_l = []
c_file_l       = []
h_file_l       = []
cpp_file_l     = []
hpp_file_l     = []
scratch        = []
# If a list of files was given, populate lists with that
if filenames:
    for f in filenames:
        path = os.getcwd()
        scratch.append(path + '/' + f)
    if (language  == 'CXX'):
        cpp_file_l     = scratch
    if (language  == 'C'):
        c_file_l       = scratch
    if (language  == 'F'):
        fortran_file_l = scratch
# else glob in the invocation directory
else:
    pwd = os.getcwd()
    for path, dir, files in os.walk(pwd):
        for file in files:
            if file[-4:] == '.F90':
                fortran_file_l.append(path + '/' + file)
            if file[-4:] == '.f90':
                fortran_file_l.append(path + '/' + file)
            if file[-2:] == '.F':
                fortran_file_l.append(path + '/' + file)
            if file[-2:] == '.c':
                c_file_l.append(path + '/' + file)
            if file[-2:] == '.h':
                h_file_l.append(path + '/' + file)
            if file[-4:] == '.cpp':
                cpp_file_l.append(path + '/' + file)
            if file[-4:] == '.hpp':
                hpp_file_l.append(path + '/' + file)

# Once the lists of files are ready update the copyright notices
if fortran_file_l:
    update_notice_fortran(fortran_file_l)
if c_file_l:
    update_notice_c(c_file_l)
if h_file_l:
    update_notice_h(h_file_l)
if cpp_file_l:
    update_notice_cpp(cpp_file_l)
if hpp_file_l:
    update_notice_hpp(hpp_file_l)

# vim:et:ts=4:sw=4
