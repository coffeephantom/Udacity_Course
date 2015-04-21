#!usr/bin/python
#-*-coding:utf-8-*-
#crawler_quiz6.py
'''
定义一个添加索引的函数
'''
index=[]
def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0]==keyword:
            entry[1].append(url)
            return #这个return比较关键，好像是停止循环，和break又不太一样
    index.append([keyword,[url]])
    return index