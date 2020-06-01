#encoding:utf-8

from crh import *


def main():
    choice = u'''
    >>> Created by SongLiHong in TaiYuan, version v1.1, Enjoy！

    >>> 1. 创建公共区域目录(CRH250_cf_update)
    >>> 2. 创建VIP目录(vod)
    >>> 3. 生成播放列表(play_list.ini)
    >>> 4. 自动修改后缀(.ts 改为 .mpg )
    >>> 5. 自动重命名视频文件(去掉中文部分，只保留编号)
    >>> 6. 自动比对play_list.ini和vidieo_source，以防漏掉视频
    >>> 7. 自动查找并移动需要的视频
    >>> 8. 生成380AL播放列表
    >>> 9. 生成5型车播放列表
    '''
    print(choice)
    c = input(">>> ")
    if c == '1':
        crh_mkdir('pub')
    elif c == '2':
        crh_mkdir('vip')
    elif c == '3':
        crh_playlist('CRH250_cf_update/play.csv')
    elif c == '4':
        crh_ext('CRH250_cf_update/video_source')
    elif c == '5':
        crh_rename('CRH250_cf_update/video_source')
    elif c == '6':
        crh_diff('CRH250_cf_update/play_list.ini', 'CRH250_cf_update/video_source')
    elif c == '7':
        crh_find('CRH250_cf_update/video_source', 'e:/bingo','CRH250_cf_update/play_list.ini')
    elif c == '8':
        crh_380_play('CRH250_cf_update/play_list.ini')
    elif c == '9':
        crh_five_play('CRH250_cf_update/play_list.ini')
    else:
        print('请重新运行该脚本!')


if __name__ == '__main__':
    main()
