
from collections import defaultdict

#取得所有Emoji文件的代码，留待检查
def getEmojiValue(emoji_table_dir):
    emoji_table = defaultdict(int)
    orientData = open(emoji_table_dir, 'r', encoding='utf-8')
    i = 1
    for newline in orientData:
        while newline.find('fully-qualified     # ') > -1 or newline.find('; non-fully-qualified # ') > -1:
            startpos = newline.find('# ')+2
            #print(startpos)
            endpos = newline.find(' ',startpos+1)
            #print(endpos)
            emoji_value = newline[startpos:endpos]
            meaning = newline[endpos + 1:len(newline)]
            '''计算Unicode的十进制数值以判断Unicode范围
            #下面两行代码用于显示表情的Unicode值
            emoji_value = emoji_value.encode('unicode-escape')
            emoji_value = emoji_value.decode('utf-8')
            #print(emoji_value)
            m = emoji_value.replace('\\ufe0f', '').replace('\\u', '').replace('\\U', '')
            #print(len(m))
            if len(m) <= 8:
                try:
                    m1 = int(m,16)
                except:
                    m1 = m
            else:
                m1 = 0
            #print(m1)
            print(m1,m,emoji_value)
            # 计算结束 '''
            emoji_table[emoji_value] = meaning.replace('\n','')
            #print(meaning)
            #print(emoji_value+':'+meaning)
            newline = orientData.readline()
            i += 1
    print('Emoji表情代码共：'+str(i)+'个。')
    #print(emoji_table)
    return emoji_table
def getEmojiValueFromWechat(emoji_table_dir):
    emoji_table = defaultdict(int)
    orientData = open(emoji_table_dir, 'r', encoding='utf-8')
    i = 1
    for newline in orientData:
        while newline.find('fully-qualified     # ') > -1 or newline.find('; non-fully-qualified # ') > -1:
            startpos = newline.find('# ')+2
            #print(startpos)
            endpos = newline.find(' ',startpos+1)
            #print(endpos)
            emoji_value = newline[startpos:endpos]
            #下面两行代码用于显示表情的Unicode值
            #emoji_value = emoji_value.encode('unicode-escape')
            #emoji_value = emoji_value.decode('utf-8')
            meaning = newline[endpos + 1:len(newline)]
            #print(emoji_value)
            emoji_table[emoji_value] = meaning.replace('\n','')
            #print(meaning)
            #print(emoji_value+':'+meaning)
            newline = orientData.readline()
            i += 1
    print('Emoji表情代码共：'+str(i)+'个。')
    #print(emoji_table)
    return emoji_table
# 手动创建表情映射表，然后将映射表读取到tbl2中
def getEmojiValueContrast(emoji_table_dir):
    emoji_table = defaultdict(int)
    orientData = open(emoji_table_dir, 'r', encoding='utf-8')
    i = 0
    for newline in orientData:
        while newline.find(': ') > -1:
            #print(newline)
            startpos = newline.find(':')+1
            #print(startpos)
            endpos = newline.find(':',startpos+1)
            #print(endpos)
            emoji_value = newline[startpos:endpos]
            #emoji_value = emoji_value.encode('unicode-escape')
            #print(emoji_value)
            value2 = newline[endpos + 2:newline.find(' ',endpos+2)]
            emoji_table[emoji_value] = value2
            #print(meaning)
            #print(emoji_value.encode('unicode-escape').decode('utf-8')+':'+value2.encode('unicode-escape').decode('utf-8'))
            newline = orientData.readline()
            i += 1
    print('映射表中Emoji表情代码共：'+str(i)+'个。')
    #print(emoji_table)
    return emoji_table

if __name__ == '__main__':
    getEmojiValueContrast('D:/python/emoji-test-add.txt')
    getEmojiValue('D:/python/emoji-test.txt')
