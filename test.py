def insertion(l=[]):
    for i in range(1,12):
        j=i
        while j>0 and l[j]<l[j-1]:
            temp=l[j]
            l[j]=l[j-1]
            l[j-1]=temp
            j=j-1
    print l

items=['I','N','S','E','R','T','I','O','N','S','O','R','T']
insertion(items)
        
