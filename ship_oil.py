__author__ = 'xyang'

# coding: utf-8

import csv

csvfile = file('//Users/xyang/Downloads/data/new_pos.csv', 'wb')
csvstcfile=file('//Users/xyang/Downloads/data/new_stc.csv', 'wb')
writer = csv.writer(csvfile,delimiter=',')
writerstc = csv.writer(csvstcfile,delimiter=',')
data=[]
for i in range(0,24):
    for j in range(0,60):
        if i<10 :
            if j<10:
                s="//Users/xyang/Downloads/data/02/0%d-0%d-pos.csv"%(i,j)
                m="//Users/xyang/Downloads/data/02/0%d-0%d-stc.csv"%(i,j)
            else:
                s="//Users/xyang/Downloads/data/02/0%d-%d-pos.csv"%(i,j)
                m="//Users/xyang/Downloads/data/02/0%d-%d-stc.csv"%(i,j)
        else:
            if j<10:
                s="//Users/xyang/Downloads/data/02/%d-0%d-pos.csv"%(i,j)
                m="//Users/xyang/Downloads/data/02/%d-0%d-stc.csv"%(i,j)
            else:
                s="//Users/xyang/Downloads/data/02/%d-%d-pos.csv"%(i,j)
                m="//Users/xyang/Downloads/data/02/%d-%d-stc.csv"%(i,j)
        print(i,j)

        readerm=csv.reader(open(m))
        for linem in readerm:
            # a,b,c,e,f,c = linem.split(",")
            if linem[0]=='308248000':
                # datam=[linem,str(i),str(j)]
                linem.append(str(i))
                linem.append(str(j))
                # datam=datam+[str(i)]
                # datam=datam+[str(j)]
                # datam.insert(0,str(i))
                # datam.insert(0,str(j))
                # datam2=[str(i),str(j)]
                # datam3=data+datam2
                print linem
                datam=[linem]
                writerstc.writerows(datam)
                # writer.writerows("%d",)%i
                # writer.writerows(j)

        reader = csv.reader(open(s))
        for line in reader:
            # o,p,q,r,s,t = line.split(",")
            if line[0]=='308248000':
                line.append(str(i))
                line.append(str(j))
                # data=[line,str(i),str(j)]
                # data2=[str(i),str(j)]
                # data3=data+data2
                print line
                data=[line]
                writer.writerows(data)
csvfile.close()
csvstcfile.close()
