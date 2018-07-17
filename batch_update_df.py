
# -*- coding: utf-8 -*-
import pandas as pd
import operator
import re

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    regax= r'[\u4e00-\u9fff]+'
    if re.match(regax,uchar):
        return True
    else:
        return False

def is_digit(uchar):
    """判断一个unicode是否是汉字"""
    regax= r'\d'
    if re.match(regax,uchar):
        return True
    else:
        return False

# 路径
path= r'E:\PyPro\Reborn\data\iu_fix2.txt'
df = pd.read_csv(path,delimiter=',')

labdic= ["专业",'公安','司法',"大交通","文教卫","智能楼宇","能源","运营商","金融"]
SAVE = False
while True:
    x= input()
    if is_chinese(x):
        print(df[df.old.str.contains(x,regex =True)].sort_values('label'))
        count = df[df.old.str.contains(x,regex =True)].groupby(['label']).old.count()
        label = count.idxmax()
        print(sorted(count.to_dict().items(),key=lambda x:x[1],reverse=True))
        print(label)
        lastinput  = x
        print("input a number and you will get class u wanted ")
    elif is_digit(x):
        if len(x)==1:
            print(df.loc[(df.old.str.contains(lastinput, regex=True)& (df.label==labdic[int(x)]))])
            print("set to another class")
            x1 =input()
            if x1=='':
                df.loc[(df.old.str.contains(lastinput, regex=True) & (df.label == labdic[int(x)])), 'label'] = label
            else:
                df.loc[(df.old.str.contains(lastinput, regex=True) & (df.label == labdic[int(x)])), 'label'] = labdic[int(x1)]
            print(df.loc[(df.old.str.contains(lastinput, regex=True))])
        else:
            print(df.loc[int(x)])
            print("set to another class")
            x1 = input()
            if x1=='':
                df.loc[int(x), 'label'] = label
            else:
                df.loc[int(x), 'label'] = labdic[int(x1)]
            print(df.loc[int(x)])
    # save the update
    elif x=='s':
        SAVE=True
        break
    # quit without save
    elif x=='q':
        break
    else:
        'input wrong type...'

if SAVE:
    name3= r'E:\PyPro\Reborn\data\iu_fix3.txt'
    df.to_csv(name3,',',na_rep="0",header=True,index=False)
    print('update the iufix3')
