import os
fileNames = os.listdir("/home/adisababa/Dropbox/The Village")
count = 0
orig_path = os.getcwd()
os.chdir("/home/adisababa/Dropbox/The Village")
for i in fileNames:
    print("old name "+ i)
    os.rename(i,"the_village_" + (str)(count))
    print("new Name " + "the_village_" + (str)(count))
    count = count + 1
os.chdir(orig_path)
print ("Count: "+ (str)(count))
