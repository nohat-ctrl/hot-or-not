import os

folders = input("How many folders> ")
os.system("sudo mkdir ../rated_images")
for x in range(1,int(folders)+1):
    os.system("sudo mkdir ../rated_images/"+str(x))