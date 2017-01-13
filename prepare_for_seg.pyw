def read_dic():
    ff=open("msr.txt","r")
    content=ff.read()
    list00=content.split("\n")
    content="".join(list00)
    global list01
    list01=content.split("  ")
    m=0
    for item in list01:
        if item=="":
            m+=1
    for i in range(m):
        list01.remove("")
    ff.close()

def tongji_dic():
    global list01
    global list02
    list02=[]
    for item in list01:
        if (len(item)==1):
            list02.append((item,"S"))
        if (len(item)==2):
            list02.append((item[0],"B"))
            list02.append((item[1],"E"))
        if (len(item)>=3):
            list02.append((item[0],"B"))
            for i in range(1,len(item)-1):
                list02.append((item[i],"M"))
            list02.append((item[len(item)-1],"E"))
    # ff1=open("biaozhu_dic.txt","w")
    # for i in range(len(list02)):
    #     ff1.write(str(list02[i])+"\n")
    # ff1.close()

def count_dic():
    global diction
    diction={}
    global list02
    for i in range(len(list02)):
        diction[list02[i]]=diction.get(list02[i],0)+1
    ff2=open("biaozhu_dic01.txt","w")
    bili=0
    for key,val in diction.items():
        bili=val/len(list02)
        if key[1]=="S":
            diction[key]=bili/0.2478739438227906
        if key[1]=="B":
            diction[key]=bili/0.31600130845620683
        if key[1]=="M":
            diction[key]=bili/0.12012343926479574
        if key[1]=="E":
            diction[key]=bili/0.31600130845620683
    for key,val in diction.items():
        ff2.write(str(key)+str(val)+"\n")

def gailv_yin():
    global list02
    ff4=open("gailv_out.txt","w")
    num=0
    for item in list02:
        if item[1]=="S":
            num=num+1
    gailvS=num/len(list02)
    ff4.write("S  "+str(gailvS)+"\n")
    num=0
    for item in list02:
        if item[1]=="B":
            num=num+1
    gailvB=num/len(list02)
    ff4.write("B  "+str(gailvB)+"\n")
    num=0
    for item in list02:
        if item[1]=="M":
            num=num+1
    gailvM=num/len(list02)
    ff4.write("M  "+str(gailvM)+"\n")
    num=0
    for item in list02:
        if item[1]=="E":
            num=num+1
    gailvE=num/len(list02)
    ff4.write("E  "+str(gailvE)+"\n")
    ff4.close()

def gailv_yinafteryin():
    global list02
    numSS=0
    numSB=0
    numBE=0
    numBM=0
    numMM=0
    numME=0
    numEB=0
    numES=0
    for i in range(1,len(list02)):
        if list02[i-1][1]=="S" and list02[i][1]=="S":
            numSS=numSS+1
        if list02[i-1][1]=="S" and list02[i][1]=="B":
            numSB=numSB+1
        if list02[i-1][1]=="B" and list02[i][1]=="E":
            numBE=numBE+1
        if list02[i-1][1]=="B" and list02[i][1]=="M":
            numBM=numBM+1
        if list02[i-1][1]=="M" and list02[i][1]=="M":
            numMM=numMM+1
        if list02[i-1][1]=="M" and list02[i][1]=="E":
            numME=numME+1
        if list02[i-1][1]=="E" and list02[i][1]=="B":
            numEB=numEB+1
        if list02[i-1][1]=="E" and list02[i][1]=="S":
            numES=numES+1
    gailvSS=numSS/(len(list02)-1)
    gailvSB=numSB/(len(list02)-1)
    gailvBE=numBE/(len(list02)-1)
    gailvBM=numBM/(len(list02)-1)
    gailvMM=numMM/(len(list02)-1)
    gailvME=numME/(len(list02)-1)
    gailvEB=numEB/(len(list02)-1)
    gailvES=numES/(len(list02)-1)
    ff3=open("gailv_out01.txt","w")
    ff3.write("SS  "+str(gailvSS)+"\n")
    ff3.write("SB  "+str(gailvSB)+"\n")
    ff3.write("BE  "+str(gailvBE)+"\n")
    ff3.write("BM  "+str(gailvBM)+"\n")
    ff3.write("MM  "+str(gailvMM)+"\n")
    ff3.write("ME  "+str(gailvME)+"\n")
    ff3.write("EB  "+str(gailvEB)+"\n")
    ff3.write("ES  "+str(gailvES)+"\n")
    ff3.close()

def count_dicplus():
    global dictionplus
    dictionplus={}
    wordbase={}
    for i in range(1,(len(list02))):
        dictionplus[(list02[i-1][0],list02[i][0],list02[i][1])]=dictionplus.get((list02[i-1][0],list02[i][0],list02[i][1]),0)+1
        wordbase[(list02[i-1][0],list02[i][0])]=wordbase.get((list02[i-1][0],list02[i][0]),0)+1
    bili=0
    for key,val in dictionplus.items():
        if val<=7:
            pass
        else:
            bili=val/wordbase[(key[0],key[1])]
            dictionplus[key]=bili
    ff5=open("biaozhu_dic02.txt","w")
    for key,val in dictionplus.items():
        ff5.write(str(key)+str(val)+"\n")

def main():
    global list01
    read_dic()
    global list02
    tongji_dic()
    global diction
    count_dic()
    gailv_yin()
    gailv_yinafteryin()
    global dictionplus
    count_dicplus()

main()