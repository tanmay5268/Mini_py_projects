import hashlib
from difflib import SequenceMatcher

def filechecker(file1,file2):
    #----------------------------
    h1=hashlib.sha1()
    with open(file1,"rb") as file:
        chunks=0
        while chunks!= b'':
            chunks = file.read(1024)
            h1.update(chunks)
    #----------------------------
    h2 =hashlib.sha1()
    with open(file2,"rb") as file:
        chunks=0
        while chunks!=b'':
            chunks = file.read(1024)
            h2.update(chunks)
    #----------------------------
    return h1.hexdigest(), h2.hexdigest()
    

info1,info2= filechecker("Untitled.jpeg","Untitled.jpeg")
if info1!=info2:
    print("FILE ARE NOT SAME")
else:
    print("FILE ARE SAME... CONGRATS")