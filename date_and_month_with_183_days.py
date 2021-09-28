da=int(input())
mon=input()
d={'jan':31,'feb':29,'mar':31,'apr':30,'may':31,'jun':30,'july':31,'aug':31,'sept':30,'oct':31,'nov':30,'dec':31}
count=183
val=d[mon]-da
y=0
tot=0
day=0
while(y<=1):
    ok=0
    if day==1:
        ok=1
    for i in d.keys():
        if ok ==1:
            tot+=d[i]
            day=1
        if i==mon:
            tot+=val
            ok=1
       
        if (tot>count):
            diff=d[i]-(tot-count)+1
            month=i
            print(diff,month)
            day=2
            break
    if day==2:
        break
    y+=1
