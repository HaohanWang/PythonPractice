sp=[line.strip() for line in open("special.txt")]
text = [line.strip() for line in open("dict.txt")]
dic = {}
for line in text:
	if "," in line:
		item = line.split(",")
		dic[item[0].strip()]=item[1].strip()[0]

para=[]
text = [line.strip() for line in open("text.txt")]
for line in text:
        word=line.split(" ")
        for i in range(len(word)):
                para.append(word[i])
for i in range(len(para)):
        if i<len(para) and para[i] in dic:
                if dic[para[i]]=="a":
                        if para[i+1]==sp[0]:
                                del para[i+1]
                        else:
                                para[i]=para[i]+sp[0]
                if i+1<len(para) and para[i+1] in dic and para[i] in dic:
                        #print para[i+1]
                        if dic[para[i]]=="n" and dic[para[i+1]]=="n":
                                para[i]=para[i]+sp[0]
                

fw = open("target.txt", "w")
fw.writelines(para)
pause = raw_input("pause")

