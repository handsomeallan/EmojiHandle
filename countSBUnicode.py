#用于计算SoftBankEmoji的数值范围
with open('data\emoji.txt','r',encoding='utf-8') as f:
    for line in f:
        line = line.split()
        try:
            print(line[1])
            print(int(line[1],16))
        except:
            print(line)