# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 11:20
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : human_vs_pc.py
# 人和机器进行猜拳游戏写一段程序，首先选择角色：1 曹操 2张飞 3 刘备，
# 然后选择的角色进行猜拳：1剪刀 2石头 3布 玩家输入一个1-3的数字
# ；然后电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果（ 1剪刀 2石头 3布 ） ，
# 双方出拳完毕后：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,
# 然后提示用户是否继续？按y继续，按n退出。
# 最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
import random
role_dict={'1':'曹操','2':'张飞','3':'刘备'}
fist_dict={'1':'剪刀','2':'石头','3':'布'}


#选择角色
def choose_role():
    while True:
        role_num=input('请选择你要的角色：1 曹操 2张飞 3 刘备')
        if role_num in ['1','2','3']:
            role_name=role_dict[role_num]
            return role_name#角色的值返回
        else:
            print('角色选择只能输入1 2 3')
            continue

def human_fist(role_name):
    while True:
        human_fist_num=input('请出拳：1剪刀 2石头 3布')
        if human_fist_num in ['1','2','3']:
            human_fist_value=fist_dict[human_fist_num]
            print("{}出拳为：{}".format(role_name,human_fist_value))
            return int(human_fist_num)
        else:
            print('出拳只能输入1 2 3')
            continue

def pc_fist():
      #pc出拳
    pc_fist_num=random.randint(1,3)#产生的是整数
    print('pc出拳为：{}'.format(fist_dict[str(pc_fist_num)]))
    return pc_fist_num

def human_vs_pc():
    human_win=0#角色赢的次数
    pc_win=0#pc赢的次数
    plain=0#平局的次数
    while True:
        #选择角色
        role_name=choose_role()
        #角色出拳
        human_fist_num=human_fist(role_name)
        #pc出拳：
        pc_fist_num=pc_fist()

        if int(human_fist_num)-pc_fist_num in [-2,1]:
            #human赢
            print("{}赢了！".format(role_name))
            human_win+=1
        elif int(human_fist_num)-pc_fist_num in [-1,2]:
            print('pc赢了！')
            pc_win+=1
        else:
            print('双方平局！')
            plain+=1

        choice=input('是否要继续：n 退出，任意键继续！')
        if choice=='n':
            break
        else:
            continue
    print('{}赢了{}局，pc赢了{}局，平局{}'.format(role_name,human_win,pc_win,plain))


human_vs_pc()