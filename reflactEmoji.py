'''
获取SoftBank与WeChat的Emoji映射表
'''

from collections import defaultdict

frequency = defaultdict(int)
frequency1 = defaultdict(int)
frequency2 = defaultdict(int)

def getReflactTbl():
    frequencies = defaultdict(int)
    with open('data\emoji.txt', 'r', encoding='utf-8-sig') as f:
        for line in f:
            line = line.split()
            frequencies[line[0]] = line[1]
        print(frequencies)
    return frequencies

def getStandordTbl():
    frequency1 = defaultdict(int)
    with open('data\emoji-test.txt', 'r', encoding='utf-8-sig') as f:
        for newline in f:
            while newline.find('fully-qualified     # ') > -1 or newline.find('; non-fully-qualified # ') > -1:
                startpos = newline.find('# ') + 2
                # print(startpos)
                endpos = newline.find(' ', startpos + 1)
                # print(endpos)
                meaning = newline[startpos:endpos]
                emoji_value = newline[endpos + 1:len(newline)]
                emoji_value = meaning.encode('unicode-escape').decode('utf-8').replace('\\U','').upper()
                frequency1[meaning] = emoji_value.replace('\n', '')
                newline = f.readline()
    print(frequency1)
    return frequency1
def getWechatTbl():
    frequency2 = defaultdict(int)
    with open('data\emoji-wechat.txt', 'r', encoding='utf-8-sig') as f:
        for newline in f:
            while newline.find('fully-qualified     # ') > -1 or newline.find('; non-fully-qualified # ') > -1:
                startpos = newline.find('# ') + 2
                # print(startpos)
                endpos = newline.find(' ', startpos + 1)
                # print(endpos)
                emoji_value = newline[startpos:endpos]
                meaning = emoji_value.encode('unicode-escape').decode('utf-8').replace('\\u','').upper()
                frequency2[meaning] = emoji_value
                newline = f.readline()
    print(frequency2)
    return frequency2
frequency = getReflactTbl()
frequency1 = getStandordTbl()
frequency2 = getWechatTbl()

#print(frequency2[])

result = defaultdict(int)
i = 0
list = []
for s in frequency:
    list.append(s)
#print(list)
list2 = []

# for s in frequency1:
#     if frequency1[s] in frequency:
#         print(s)
#print(frequency.values())
for s in frequency2:
    if frequency2[s] in frequency.values():
        result[s] = frequency2[s]

for s in frequency1:
    if frequency1[s] in frequency.keys():
        print(frequency1[s],frequency[frequency1[s]])
        if frequency2[frequency[frequency1[s]]] != 0:
            result[s] = frequency2[frequency[frequency1[s]]]
print(result)

file = open('data\emoji-reflact.txt','w',encoding = 'utf-8')
for s in result:
    res = 'meaning1:'+result[s]+': '+ s + ' ' + 'meaning2\n'
    print(res)
    file.write(res)