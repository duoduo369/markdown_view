#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Naval Fate.

Usage:
  markdown_view.py <markdown_file>
  markdown_view.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

import subprocess

def trans_command(command):
    return command.split()

def exec_command(command):
    print subprocess.check_output(command, shell=True), '\n'

def get_html_name(md_file):
    return md_file.split('.')[0] + '.html'

def markdown2(md_file):
    html_file = get_html_name(md_file)
    command = 'markdown2 {md_file} > {html_file}'.format(
        md_file=md_file, html_file=html_file)
    exec_command(command)

def browser_markdown(md_file):
    html_file = get_html_name(md_file)
    command = 'python -m webbrowser -t {html_file} &'.format(html_file=html_file)
    exec_command(command)

def run(md_file):
    markdown2(md_file)
    browser_markdown(md_file)

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.0')
    md_file = arguments.get('<markdown_file>', None)
    if md_file:
        run(md_file)
