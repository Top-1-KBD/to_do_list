#!C:\Users\erezz\OneDrive\Documents\BGD Kit Big Data\to_do_list\venv\Scripts\python.exe

# Author:
# Contact: grubert@users.sf.net
# Copyright: This module has been placed in the public domain.

"""
man.py.
======

A module for converting ReStructuredText to man pages.

This module provides a simple command line interface. It uses the man page
writer to output from ReStructuredText source.
"""

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except Exception:
    pass

from docutils.core import publish_cmdline, default_description
from docutils.writers import manpage

description = ("Generates plain unix manual documents.  "
               + default_description)

publish_cmdline(writer=manpage.Writer(), description=description)
