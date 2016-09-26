#!/usr/bin/env python
#_*_coding:utf-8_*_



import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weibo.settings")

    from Intrac.management import execute_from_command_line

    execute_from_command_line(sys.argv)