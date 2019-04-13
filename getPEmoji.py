
import os
import CreateTable
import getEmoji
from collections import defaultdict
import emojis
import re

frequencies = defaultdict(int)

#判断是否是表情
def isEmoji(content):
    if not content:
        return False
    if u"\uE000" <= content and content <= u"\uE900":
        return True
    if u"\U0001F000" <= content and content <= u"\U0001FA99":
        return True
    #以下代码被上面的范围包含了
    if u"\U0001F600" <= content and content <= u"\U0001F64F":
        return True
    elif u"\U0001F300" <= content and content <= u"\U0001F5FF":
        return True
    elif u"\U0001F680" <= content and content <= u"\U0001F6FF":
        return True
    elif u"\U0001F1E0" <= content and content <= u"\U0001F1FF":
        return True
    else:
        return False

def identifyEmoji(desstr):
    '''
    通过正则表达式识别表情，失败
    '''
    co = re.compile(r'\\u\w{4}|\\U\w{8}')
    print(co.findall(desstr))
    if len(co.findall(desstr)):
        return True
    else:
        return False
#获取txt文件列表
def getFilesNames(dir):
    fileNames = os.listdir(dir)
    return fileNames

#依次检查每个字符是否是表情符号
def getChar(filename,tbl,tbl2):
    file = open(filename,'r',encoding='utf-8')
    fileSort = open('d:/python/result-emoji-sort.txt', 'a+', encoding='utf-8')
    frequency = defaultdict(int)
    dicwrite = open('d:/python/result-emoji.txt', 'w', encoding='utf-8')
    f = 0 #用于存储Emoji表情数量
    emojiDict = ['嘿哈','捂脸','奸笑','机智','皱眉','耶','红包','發','小狗','福','鸡']
    for line in file:
        # 查找所有汉字表示的Emoji表情
        while line.find('[') > -1 and line.find(']') > -1:
            startpos=line.find('[')
            endpos=line.find(']')
            word=line[startpos+1:endpos]
            word = str(word).replace('表情', '')
            if word in emojiDict:
                frequency[word]+=1
                f+=1
                frequencies[word]+=1
            line = line[endpos + 1:]
        # 查找非汉字的Emoji表情
        i = 0 #控制循环进行
        while i < len(line) :
            s = line[i]
            i += 1
            if(isEmoji(s)):
                #判断表情符号是否为微信内，先手动创建映射表tbl2，若是的话，到标准库中去匹配，标准库中值加1
                if s in tbl2:
                    s = tbl2[s]
                    #print(tbl[s])
                frequency[s]+=1
                frequencies[s]+=1
                # 判断表情符号是否在标准库中，若不在，显示其Unicode值
                if s not in tbl:
                    print(s.encode('unicode-escape').decode('utf-8'))
                    #print(tbl[s])
                    tbl[s] = s.encode('unicode-escape').decode('utf-8')  #将Unicode库中无法识别的表情转码显示其Unicode值，推测该部分表情来自于第三方输入法
                #print(s,tbl[s],line.replace('\n',''))
                f += 1
                #print(s)
        continue
    print('Emoji表情共：' + str(f) + '个。')
    fileSort.write(filename+'    '+str(f)+'\n')
    sorteddic = sorted(frequencies.items(), key=lambda e: e[1], reverse=True)
    for item in sorteddic:
        if isEmoji(item[0]):
            #print(tbl[item[0]])
            dicwrite.write(tbl[item[0]] + '\t' + str(item[1]) + '\n')  # 待优化，重复写了多次
        else:
            dicwrite.write(item[0] + '\t' + str(item[1]) + '\n') #待优化，重复写了多次
    #print(frequency)
    return frequency
def getChar2(filename,tbl,tbl2):
    file = open(filename,'r',encoding='utf-8')
    frequency = defaultdict(int)
    dicwrite = open('d:/python/result-emoji.txt', 'w', encoding='utf-8')
    f = 0 #用于存储Emoji表情数量
    emojiDict = ['嘿哈','捂脸','奸笑','机智','皱眉','耶','红包','發','小狗','福','鸡']
    for line in file:
        # 查找所有汉字表示的Emoji表情
        newline = line
        while newline.find('[') > -1 and newline.find(']') > -1:
            startpos=newline.find('[')
            endpos=newline.find(']')
            word = newline[startpos+1:endpos]
            if word == '胜利表情':
                print(newline)
            word = str(word).replace('表情', '')
            frequency[word]+=1
            frequencies[word]+=1
            newline = newline[endpos + 1:]
        # 查找非汉字的Emoji表情
        i = 0 #控制循环进行
        while i < len(line) :
            s = line[i]
            i += 1
            if(isEmoji(s)):
                #判断表情符号是否为微信内，先手动创建映射表tbl2，若是的话，到标准库中去匹配，标准库中值加1
                if s in tbl2:
                    s = tbl2[s]
                    #print(tbl[s])
                frequency[s]+=1
                frequencies[s]+=1
                # 判断表情符号是否在标准库中，若不在，显示其Unicode值
                if tbl[s] == 0:
                    tbl[s] = s.encode('unicode-escape').decode('utf-8')  #将Unicode库中无法识别的表情转码显示其Unicode值，推测该部分表情来自于第三方输入法
                #print(s,tbl[s],line.replace('\n',''))
                f += 1
                #print(s)
        continue
    print('Emoji表情共：' + str(f) + '个。')
    sorteddic = sorted(frequencies.items(), key=lambda e: e[1], reverse=True)
    for item in sorteddic:
        if isEmoji(item[0]):
            #print(tbl[item[0]])
            dicwrite.write(tbl[item[0]] + '\t' + str(item[1]) + '\n')  # 待优化，重复写了多次
        else:
            dicwrite.write(item[0] + '\t' + str(item[1]) + '\n') #待优化，重复写了多次
    #print(frequency)
    return frequency

def emojiCount(file):
    file = open(file, 'r', encoding='utf-8')
    i = 0
    for line in file:
        if emojis.count(line) > 0:
            i+=1
    print(i)

#将结果写入到txt结果文件
def writeToText(tbl,frequency,filename):
    if(len(frequency)!=0):
        dicwrite = open(filename, 'w', encoding='utf-8')
        sorteddic = sorted(frequency.items(), key=lambda e: e[1], reverse=True)
        for item in sorteddic:
            if tbl[item[0]] == 0:
                #dicwrite.write(item[0] + '\t' + str(item[0]) + '\t' + str(item[1]) + '\n')
                dicwrite.write(str(item[0]) + '(' + str(item[1]) + '),')
            else:
                #dicwrite.write(item[0] + '\t' + tbl[item[0]] + '\t' + str(item[1]) + '\n')
                dicwrite.write(str(tbl[item[0]]) + '(' + str(item[1]) + '),')


# tbl = CreateTable.getEmojiValue('D:/python/emoji_unicode_2018.1.25.txt')

if __name__ == '__main__':
    tbl = CreateTable.getEmojiValue('D:/python/emoji-test.txt') #获取EmojiUnicode值表
    tbl2 = CreateTable.getEmojiValueContrast('D:/python/emoji-test-add.txt')
    #tbl = CreateTable.getEmojiValue2('D:/python/emoji_table.txt')  # 获取EmojiUnicode值表
    print(tbl)
    print(tbl2)
    dir = 'D:/1Study/8论文草稿/00_聊天记录分析/00_论文使用数据/' #待分析数据列表
    systemEmoji_Dir = 'd:/python/System_Emoji_result/' #系统表情存储目录
    Emoji_dir = 'd:/python/Emoji_result/' #Emoji表情存储目录
    filenames = getFilesNames(dir) #获取待分析的文件名

    for file in filenames:
        filename = file
        file = 'D:/1Study/8论文草稿/00_聊天记录分析/00_论文使用数据/'+file;
        print(file)
        writeToText(tbl,getChar(file,tbl,tbl2),Emoji_dir+filename) #写入Emoji表情结果
        #getEmoji.writeToText(systemEmoji_Dir+filename,getEmoji.getList(file)) #写入系统表情结果文件