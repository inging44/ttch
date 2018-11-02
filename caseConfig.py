#coding = utf-8
from configparser import ConfigParser
import os

class CaseConfig:
    def __init__(self):
        path = os.getcwd()
        filename = os.path.join(path, 'caselist.conf')
        self.casecfg = ConfigParser()
        self.casecfg.read(filename)
        # self.casecfg.get('run_mode', 'run_mode')

    def get_case_list(self):
        case_list = []
        if self.get_run_mode() == '0':
            case_list = self.casecfg.get('case_list', 'run_list')
        elif self.get_run_mode() == '1':
            print("run all") 
            case_list = self.casecfg.get('case_list', 'case_all')
            
        return case_list

    def get_run_mode(self):
        return self.casecfg.get('run_mode', 'run_mode')