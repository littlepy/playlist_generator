import csv
import os
import re
from configparser import ConfigParser
import time
import shutil
from sys import exit


def crh_five_rename():
    file_names = os.listdir('.')
    file_names.remove(__file__)
    for d in file_names:
        newname = d.split('_')[1]
        os.rename(d, newname)


def crh_five_move():
    file_names = os.listdir('.')
    file_names.remove(__file__)
    for d in file_names:
        os.chdir(d+'/VIDEO_TS/')
        cwd = os.getcwd()
        print(cwd)
        for f in os.listdir('.'):
            # if f == 'VTS_01_0.VOB':
                # os.remove(f)
            shutil.move(f, '../')
        os.chdir('../../')

def crh_five_del():
    file_names = os.listdir('.')
    file_names.remove(__file__)
    for d in file_names:
        os.chdir(d)
        os.remove('VTS_01_0.VOB')
        os.chdir('../')
    
        
if __name__ == '__main__':
    crh_five_rename()
    crh_five_move()
    crh_five_del()