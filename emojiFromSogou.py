
# 测试Emoji表情符号包Emojis的功能

import emojis
print(emojis.count('Python is fun 👍'))

# 读取搜狗输入法的表情示例，验证搜狗输入法的表情代码，的确为Unicode，如U+0001F601

from collections import defaultdict
file = open('data\sogouw.txt','w',encoding='utf-8-sig')
with open('data\sogou.txt','r',encoding='utf-8-sig') as f:
    i = 0
    for line in f:
        line = line.replace(' ','\n')
        while i < len(line):
            file.write(line[i])
            i+=1
file.close()
frequencies = defaultdict(int)
with open('data\sogouw.txt','r',encoding = 'utf-8-sig') as f:
    for line in f:
        line = line.replace('\n','')
        a = line.encode('unicode-escape').decode('utf-8')
        print(line, a)
        a = a.replace('\\u','').replace('\\U','').replace('feff','')
        # 计算Sogou Unicode的十进制值以划定范围
        try:
            b = int(a,16)
        except:
            print(a)
        print(b)

# 统计搜狗输入法表情测试文档中Emoji表情的个数
def emojiCount(file):
    file = open(file, 'r', encoding='utf-8')
    i = 0
    for line in file:
        if emojis.count(line) > 0:
            i+=1
    print(i)

emojiCount('data\sogouw.txt')
