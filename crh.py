#!/usr/bin/python
#coding:utf-8



'''
该脚本实现了以下功能：

1.自动生成节目列表文件(play_list.ini)
2.自动重命名影视文件(去掉中文，只留编号)
3.自动比对节目列表与影视文件的一致性
4.自动创建CF卡目录
5.自动修改扩展名(将xxx.ts改为xxx.mpg, 针对公共区域)

作者：宋利宏
日期：2014.6.28
地点：太原
版本：v1.1
'''


import csv
import os
import re
from configparser import ConfigParser
import time
import shutil
from sys import exit


#auto make dir
def crh_mkdir(choice):
    if choice == 'pub':
        rootdir = 'CRH250_cf_update'
        os.mkdir(rootdir)
        os.chdir(rootdir)
        os.mkdir('audio_source1')
        os.mkdir('audio_source2')
        os.mkdir('audio_source3')
        os.mkdir('video_source')
    elif choice == 'vip':
        rootdir = 'vod'
        os.mkdir(rootdir)
        os.chdir(rootdir)
        os.mkdir('audio')
        os.mkdir('video')
    else:
        exit(1)


# auto create playlist

def crh_playlist(csv_file):
    with open(csv_file, 'rb') as csv_file:
        with open('play_list.ini', 'wb') as play_list:
            csv_file.seek(0)
            r = csv.reader(csv_file)
            cf = ConfigParser()
            # cf.read(play_list)
            cf.add_section('LIST-0')
            cf.set('LIST-0', 'list_name', time.strftime("%Y%m%d", time.localtime()))
            for row in r:
                cf.set('LIST-0', 'video-{}'.format(row[0]), '{}.mpg'.format(row[1]))
            cf.write(play_list)


# auto find the difference if it exists

def crh_diff(play_list, video_path):
    error = 0
    cf = ConfigParser()
    cf.read(play_list)
    items = cf.items('LIST-0')
    for i in items:
        if i[0] == 'list_name':
            items.pop(items.index(i))
    #items.remove(items[items.index(('list_name', time.strftime("%Y%m%d", time.localtime())))])
    videos = os.listdir(video_path)
    needed = []
    for item in items:
        if item[1] not in videos:
            print('{}'.format(item[1]))
            needed.append(item[1])
            error += 1
    needed = sorted(set(needed))
    if needed:
        with open('needed.txt', 'wb') as f:
            for i in needed:
                f.write(i+'\n')
    if error > 0:
        print('please add the {} videos above'.format(error))
    else:
        print('Bingo, all videos in the play_list is also in the video_souce dir!')


#modify the extention of video files

def crh_ext(ts_dir):
    os.chdir(ts_dir)
    for file in os.listdir('.'):
        file_path = os.path.abspath(file)
        name, ext = os.path.splitext(file_path)
        new_name = "{}.mpg".format(name,)
        print(new_name)
        os.rename(file, new_name)


#auto rename the video files

def crh_rename(dir):
    os.chdir(dir)
    patten = re.compile(r'[A-Z]+[0-9]+')
    for file in os.listdir('.'):
        file_path = os.path.abspath(file)
        name, ext = os.path.splitext(file_path)
        result = patten.match(file)
        if result:
            new_name = '{}.mpg'.format(result.group(),)
            os.rename(file, new_name)
            print(new_name)
        else:
            continue


#auto find and copy the videos in the playlist to the target dir

def crh_find(source_dir, target_dir, play_list):
    cf = ConfigParser()
    cf.read(play_list)
    items = cf.items('LIST-0')
    for i in items:
        if i[0] == 'list_name':
            items.pop(items.index(i))
    #items.remove(items[items.index(('list_name', time.strftime("%Y%m%d", time.localtime())))])
    play_items = []
    for i in items:
        play_items.append(i[1])
    play_items = sorted(set(play_items))
    print(play_items)
    videos = os.listdir(source_dir)
    os.chdir(source_dir)
    for item in play_items:
        if item in videos:
            shutil.move(item, target_dir)

#五型车节目单
def crh_five_play(play_list):
    cf = ConfigParser()
    cf.read(play_list)
    items = cf.items('LIST-0')
    for i in items:
        if i[0] == 'list_name':
            items.pop(items.index(i))
    #items.remove(items[items.index(('list_name', time.strftime("%Y%m%d", time.localtime())))])
    with open('2.txt', 'wb') as f:
        for i in items:
            name = i[1].split('.')[0]
            f.write(name+';\r\n')


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
            shutil.move(f, '../')
        os.chdir('../../')
        
def crh_five_del():
    file_names = os.listdir('.')
    file_names.remove(__file__)
    for d in file_names:
        os.chdir(d)
        os.remove('VTS_01_0.VOB')
        os.chdir('../')

#380AL PLAYLIST

def crh_380_play(play_list):
    cf = ConfigParser()
    cf.read(play_list)
    items = cf.items('LIST-0')
    for i in items:
        if i[0] == 'list_name':
            items.pop(items.index(i))
    with open('play.txt', 'wb') as f:
        for i in items:
            f.write(i[1]+'\r\n')

			
#make the wget list of E28/E27

def list_gen(video_dir):
	videos = os.listdir(video_dir)
	videos.remove(__file__)
	http = 'http://10.2.102.235/'
	with open('v.txt', 'wb') as f:
		for v in sorted(videos):
			f.write(http+v+'\n')
			print(http+v)