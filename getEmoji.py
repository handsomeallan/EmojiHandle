
from collections import defaultdict

frequencies = defaultdict(int) #用于保存所有群表情的总频次

def getList(filename):
    wordlist = []  # 存储获取的表情名称
    frequency = defaultdict(int)  # 定义词典，用于保存单个群的表情名称及其出现次数
    dicwrite = open('d:/python/result.txt', 'w', encoding='utf-8')
    i=0
    emojiDict = ['嘿哈', '捂脸', '奸笑', '机智', '皱眉', '耶', '红包', '發', '小狗', '福','鸡']
    notEmojiDict = ['动画','照片壁纸','视频','历史首届','小视频','祝','乐','茶','微信红包','恭','大','家','新','年','快','File','提','前','图片','反腐','军事','港澳','台湾','转账','您','在','此','1','我们将不得不通过GPS定位，对继续逗留在现场闹事的车主们立刻取消合作，以配合公共秩序安全','姓名','周末','','好消息','专家说','闹心事','别学他',' 快','暑期时间定制团','7.15-22','07.22-31','07.21-29','7.22-31','武汉','湖北生活频道','春','节','小','更新公告','正式服','资料整理','2月24日更新']
    for line in open(filename,'r',encoding='utf-8'):
        newline=line
        while newline.find('[') > -1 and newline.find(']') > -1:
            startpos=newline.find('[')
            endpos=newline.find(']')
            word=newline[startpos+1:endpos]
            #if word == '胜利表情':
            #    print(line)
            # if (word.find('Facep') > -1):
            #     print('***************' + filename)
            #     print(line)
            word = str(word).replace('表情','')
            wordlist.append(word)
            if word not in emojiDict and word not in notEmojiDict:
                frequency[word]+=1
                frequencies[word]+=1
            newline=newline[endpos+1:]
            i+=1
    print('系统表情共：' + str(i) + '个。') #找到表情的次数，即表情数量
    sorteddic = sorted(frequencies.items(), key=lambda e: e[1], reverse=True)
    #print(sorteddic)
    for item in sorteddic:
        dicwrite.write(item[0] + '\t' + str(item[1]) + '\n') #待优化，重复写了多次
    return frequency
def writeToText(toFile,frequency):
    dicwrite = open(toFile, 'w', encoding='utf-8')
    sorteddic = sorted(frequency.items(), key=lambda e: e[1], reverse=True)
    for item in sorteddic:
        #dicwrite.write(item[0] + '\t' + str(item[1]) + '\n')
        dicwrite.write(item[0] + '(' + str(item[1]) + '),')

#getList('d:/python/toHandleData.txt') #查找表情并写入wordList
#writeToText('d:/python/result.txt') #排序并写入结果文档
#print(frequency) #表情排序结果



