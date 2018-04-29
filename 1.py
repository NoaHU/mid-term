newgrade =[]
news=[]
average = []
newss=[]
t = 1
average.append(0)
average.append("平均")
with open("report.txt",encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        grades = line.split()
        a = 0
        n = 0
        for grade in grades[1:]:
            a += int(grade)
            n += 1
        grades.append(a)
        grades.append(a/n)
        newgrade.append(grades)
    new = sorted([x for x in newgrade], key= lambda x:x[-1],reverse=True)
    for eachone in new:
        eachone.insert(0,t)
        t += 1
        news.append(eachone)
    for m in range(1,12):
        b = 0
        for eachone in news:
            b += int(eachone[m+1])
        average.append(b/30)
    news.insert(0,average)
    for eachones in news:
        for n in range(1,12):
            try:
                if int(eachones[n+1]) < 60:
                    eachones[n+1] = "不合格"
            except:
                if eachones[n+1] < 60:
                    eachones[n+1] = "不合格"
        eachoness = [str(i) for i in eachones ]
        eachoness[-1] += '\n'
        newss.append(" ".join(eachoness))
with open("finalgrade.txt","w",encoding="utf-8") as f:
    f.writelines(newss)






