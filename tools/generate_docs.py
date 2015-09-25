#!/usr/bin/python
# -*- python -*-
# -*- coding: utf-8 -*-
# vim:filetype=python:
# Generates HTML docs.
# (c) Roberto Di Remigio  <roberto.d.remigio@uit.no>
# licensed under the GNU Lesser General Public License

import docopt
import os
import subprocess

def doxygen_command(*args):
    return subprocess.check_call(['doxygen'] + list(args), shell=False)


def run_doxygen(where):
    return doxygen_command(where)


def main():
    options = """
    Usage:
      ./generate_docs.py <project_dir>
      ./generate_docs.py (-h | --help)

    Options:
      <project_dir>   Directory where the Doxyfile is located.
      -h --help       Show this screen.
    """
    try:
        arguments = docopt.docopt(options, argv=None)
    except docopt.DocoptExit:
        sys.stderr.write('ERROR: bad input to %s\n' % sys.argv[0])
        sys.stderr.write(options)
        sys.exit(-1)

    build = arguments['<project_dir>']
    doxyfile = build + '/Doxyfile'
    run_doxygen(doxyfile)


if __name__ == '__main__':
    main()

# vim:et:ts=4:sw=4
