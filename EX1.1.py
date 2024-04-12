#1. To write the words in a given  file into words.txt and to create a histogram for that same given file and write it into words-histogram.txt

def histogram(myf):
    global d
    d={}
    for i in myf:
        if i not in d.values():
            d[i]=1
        else:
            d[i]=d[i]+1
            
def find_txt(directory):
    import os
    files = os.listdir(directory)
    index = 0
    myfile2=open("words.txt","a")
    myfile3=open("words-histogram.txt","a")


    while index < len(files):
        filename = files[index]
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename),encoding="utf-8") as f:
                
                myf=f.read().split()
                histogram(myf)
                for i in myf:
                    i.rstrip(".")
                    myfile2.write(i)
                    myfile2.write(" ")
            index += 1
            
        else:
            find_txt(os.path.join(directory, filename))              

    for i in d: 
        ij=i+":"
        myfile3.write(ij)
        myfile3.write(str(d[i])+"\n")
    myfile3.close()


d=r"Z:\IT C 134\Software devolepment lab\python-3.11.3-docs-text"   
find_txt(d)


