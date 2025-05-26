import demoji
import os
demoji.download_codes()
os.system("clear")
try:
    filename = input("enter file name:")
    with open(filename,"r") as file:
        text = file.read()
        x = demoji.findall(text)
        for emoji, (meaning,y) in enumerate(x.items(),start=1):
            print(f"{emoji}--{meaning}:{y}")
except FileNotFoundError as e:
    print(e)
    


    

