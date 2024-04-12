f=open("words.txt","r")
f1=open("words-histogram.txt","r")
myf1=f1.readlines()
myf=f.read().split()
ans="yes"
l=[]
while ans=="yes":
    prefix=input("Enter a prefix:")
    for i in myf:
        i=i.rstrip(".")
        try:
            if i not in l:
                if i.startswith(prefix):
                    l.append(i)
            for i in myf1:
                a=i.split(":")
                l1.append(a)
            for i in range(len(l1)):
                for j in range(len(l1)-i-1):
                    l1[j][1]<1l[j+1][1]
                    l1[j][1],l1[j+1][1]=l1[j+1][1],l1[j][1]
            for k in l1:
                print(k[0])                 
            
                
        except EOFError:
            print("No words startswith the words you have entered.")
            ans=input("Do you want to retry?(yes/no)  ")

f.close()
f1.close()
            
