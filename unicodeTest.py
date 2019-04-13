#coding=utf-8

import re


def identifyEmoji(desstr):
    '''
    识别表情
    '''

    co = re.compile(r'\\u\w{4}|\\U\w{8}')
    print(co.findall(desstr))
    if len(co.findall(desstr)):
        return True
    else:
        return False


#emojiCount('D:/1Study/8论文草稿/00_聊天记录分析/00_论文使用数据/gz02_三版百科全书.txt')
print(u'\U00010000')
a = '😁'.encode('unicode-escape').decode('utf-8')
print(a)
print(identifyEmoji(a))

"""
for i in range(0x1f600,0x1f650):
    print(chr(i),end=" ")
    if i%16==15:
        print()
"""
"""
for i in range(0x0,0x10ffff):
    print(chr(i),end=" ")
    if i%16==15:
        print()
"""

co = re.compile(r"u[\'\"]\\[Uu]([\w\"]{9}|[\w\"]{5})")

m = r'u[\'\"]\\[Uu]([\w\"]{9}|[\w\"]{5})'

m = r'ue[0-9]+'

str = 'ue415'

print(re.match(m,str).group(0))

print(re.search(co,str))

pattern = re.compile('abc')
str = 'abc is a good song for study abc'
print(re.match(pattern,str).group())


u = "好"

str2 = u.encode('unicode-escape').decode('utf-8') # 将字符串的unicode值打印出来
str = u.encode('utf-8')
str3 = u.encode('unicode-escape')
unicode = str.decode('utf-8')

print(str,str2,str3,unicode)

'''
ustring = unicode('好','utf-8')
#print(a.unicode())

# 直接定义unicode字符串，通过在字符串前加 u 的方式
unicodestring = u"Hello world"

utf8string = '好人'  # 可以这样直接写，是因为在py文件的开头写了 #encoding=utf-8, 这样在整个py
# 文件中，所有的字符串的编码编码方式都设置为了utf-8

# 将某种字符集编码的字符串转化为unicode字符串， 即“解码”
ustring = unicode(utf8string, "utf-8")

ustring  # 输出 u'\u597d\u4eba'
print(type(ustring))  # 输出 <type 'unicode'>

# 将unicode字符串转化为某种字符集编码的字符串，即“编码”
unicodestring.encode("utf-8")
ustring.encode('utf-8')

print(ustring.encode('utf-8'))  # 输出 好人， 解码到unicode和从unicode编码的字符集相同
print(ustring.encode('gbk'))  # 输出乱码 濂戒汉， 解码到unicode和从unicode编码的字符集不同

#'''