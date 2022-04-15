a=[]
sum=0
f= int (input("Enter Frames: "))
a=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]

n=len(a)
#print(n)
m=[]
c=[]
for i in range(f):
    m.append(-1)
count=0

print('Output: ')
for i in range(n):
    test=0
    p=0
    for p in range(f):
        c.append(m[p])

    if count>=f:
        count=0
    for j in range(f):
        if a[i]==m[j]:
            test=1
            break
    if test==0:
        m[count]= a[i]
        count+=1
        sum+=1
    if c==m:
        for q in range(f):
            print('HIT',end=' ')
    else:
        for q in range(f):
            if m[q]==-1:
                print("NULL",end=' ')
            else:
                print(m[q],end=' ')
    c.clear()
    print()
print("Page Fault: ",sum)
