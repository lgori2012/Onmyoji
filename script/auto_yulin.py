# coding: utf-8

import pyautogui as pi
import os
import time
import random

print("yulin")
schedule_rounds = 1200  # 300次上限

# fns = ['yl_tiaozhan_v20191226.png', 'yl_jiangli_v20191226.png', 'yl_shibai_v20191226.png']
fns = ['diaocha_v20200416.jpg', 'jiangli_v20200416.jpg']
resource_pic = '../resource/pic/'
subDir = "20200115wsw/"


def yulin():
    num_find = 0
    num_click = 0
    dura = 2
    bExist = False
    snapDir = resource_pic + subDir
    while True:
        for fn in fns:
            # print(fn)
            fp = snapDir + fn
            # print(fp, os.path.exists(fp))
            mbr = pi.locateOnScreen(fp, confidence=.95)
            # print(mbr)
            num_find += 1
            if mbr is not None:
                print(mbr, mbr[0])
                pos = centerBox(mbr)
                pos = random_click(pos)
                print(time.ctime(), pos, fn, "count:", num_click, schedule_rounds)
                pi.click(pos)
                num_click += 1

            else:
                # print(time.ctime(), 'no match')
                pass
            time.sleep(dura)
            random_time()

        if num_click >= schedule_rounds:
            print("===END===", time.ctime())
            break


def centerBox(box):
    pt = []
    pt.append(box[0] + box[2] // 2)
    pt.append(box[1] + box[3] // 2)
    return pt


def random_time(low=.1, high=1.0):
    time.sleep(random.uniform(low, high))


def random_click(pos, low=-10, high=10):
    pos[0] = pos[0] + random.randint(low, high)
    pos[1] = pos[1] + random.randint(low, high)
    return pos


if __name__ == '__main__':
    yulin()
