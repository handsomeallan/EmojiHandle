# coding=utf-8
'''
判断是否包含Emoji表情，更新Sql Server中的是否存在表情字段。
'''

import pymssql

# 根据群内数据绘制幂律分布图

def isEmoji(content):
    if not content:
        return False
    if u"\uE000" <= content and content <= u"\uE900":
        return True
    if u"\U0001F000" <= content and content <= u"\U0001FA99":
        return True
    else:
        return False


def isTextEmoji(line):
    i = 0  # 控制循环进行
    while i < len(line):
        s = line[i]
        i += 1
        if (isEmoji(s)):
            return True
    emojiDict = ['嘿哈', '捂脸', '奸笑', '机智', '皱眉', '耶', '红包', '發', '小狗', '福', '鸡']
    # 查找所有汉字表示的Emoji表情
    while line.find('[') > -1 and line.find(']') > -1:
        startpos = line.find('[')
        endpos = line.find(']')
        word = line[startpos + 1:endpos]
        word = str(word).replace('表情', '')
        if word in emojiDict:
            return True
        else:
            line = line[endpos + 1:]
def updateEmojiState(groupName):
    # 1、获取群数据
    try:
        conn = pymssql.connect(host='localhost', user='sa', password='sa', database='wechat') # 必须打开SQL Server的Tcp/IP协议才可以访问
        cur = conn.cursor()  # 数据库游标

        # groupName = '博士论坛'
        tblName = ''+ groupName +'\n'

        sql = 'select 消息 from '+ tblName;
        cur.execute(sql)
        result = cur.fetchall()
        PLNum = [n[0] for n in result]  # 表情数

        for l in PLNum:
            if l != None:
                if isTextEmoji(l):
                    sql = "update " + tblName + "set 是否包含Emoj表情 = '是' where 消息 = '" + l + "'";
                    sql2 = "update " + tblName + "set 是否包含表情 = '是' where 消息 = '" + l + "'";
                    #print(sql)
                    cur.execute(sql)
                    cur.execute(sql2)
        # 异常处理
    except pymssql.Error as e:
        print(("SQL Server Error %d: %s") % (e.args[0], e.args[1]))
    finally:
        cur.close()
        conn.commit()
        conn.close()
    #'''
    #'''
def countEmoticonNum(tblName):
    try:
        conn = pymssql.connect(host='localhost', user='sa', password='sa',
                               database='wechat')  # 必须打开SQL Server的Tcp/IP协议才可以访问
        cur = conn.cursor()  # 数据库游标

        # groupName = '博士论坛'
        tblName = '' + tblName + '\n'
        sql1 = "select count(*) from " + tblName + " where 是否包含表情 = '是'";
        sql2 = "select count(*) from " + tblName;
        cur.execute(sql1)
        result1 = cur.fetchall()
        cur.execute(sql2)
        result2 = cur.fetchall()
        print(tblName,result1[0],result2[0])
        # 异常处理
    except pymssql.Error as e:
        print(("SQL Server Error %d: %s") % (e.args[0], e.args[1]))
    finally:
        cur.close()
        conn.commit()
        conn.close()

if __name__ == '__main__':

    x = ['三版百科','自科重大','教指委','博士17班','信管校友','同学04级','老年群','老连家','滑翔伞','林州滑翔','游戏群','海大摄影']
    y = ['A1','A2','A3','B1','B2','B3','C1','C2','D1','D2','D3','D4']
    # x = ['三版百科']
    # y = ['A1']
    #i = 0
    for i in range(len(x)):
        updateEmojiState(x[i])
        countEmoticonNum(x[i])
