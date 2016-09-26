#!/usr/bin/env python
#_*_coding:utf-8_*_


import os,sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weibo.settings")

django.setup()
#from monitor.backends import data_processing,trigger_handler
from weibo import settings
from Intrac import deamon


class Manage_Handler:

    def __init__(self,argv):
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])
        self.settings_exception = None
        self.registered_actions = {
            # 'start': self.start,
            # 'stop': self.stop,
            'new_wb_dispatcher': self.new_wb_handler,
            # 'user_wb_test': self.user_wb_test,

        }

        self.argv_check()


    def argv_check(self):
        '''
        do basic validation argv checks
        :return:
        '''
        if len(self.argv) < 2:
            self.main_help_text()
        if self.argv[1] not in self.registered_actions:
            self.main_help_text()
        else:
            self.registered_actions[sys.argv[1]]()


    def new_wb_handler(self):
        '''启动新wb处理器'''
        print("--start wb dispachter---")
        dispatcher_obj = deamon.WbHandler()
        dispatcher_obj.watch_new_wbs()

    def main_help_text(self, commands_only=False):
        """
        Returns the script's main help text, as a string.
        """
        if not commands_only:
            print("supported commands as flow:")
            for k,v in self.registered_actions.items():
                print("    %s\t" % (k))
            exit()



def execute_from_command_line(argv=None):
    """
    A simple method that runs a ManagementUtility.
    """
    utility = Manage_Handler(argv)