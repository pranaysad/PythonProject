print("Goodbye, World!")

import cv2

import os

dirpath = os.getcwd()
#print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
#print("Directory name is : " + foldername)

#dirpath = dirpath + "/src"


for filename1 in os.listdir(dirpath):
    if filename1.endswith(".asm") or filename1.endswith(".py"): 
        # print(os.path.join(directory, filename))
        continue
    else:
        for filename2 in os.listdir(dirpath):
            if filename2.endswith(".asm") or filename2.endswith(".py"): 
                # print(os.path.join(directory, filename))
                continue
            else:
                if filename1!=filename2:
                    #print filename1
                    #print filename2
                    
                    a = cv2.imread(filename1)
                    b = cv2.imread(filename2)
                    
                    diff = cv2.subtract(a, b)
                    
                    if diff is None:
                        #print "diff is None"
                        #os.remove("/Users/pranaysadarangani/eclipse-workspace/dup/src/1-2.png")
                        filepath = os.path.join(dirpath,filename2)
                        print filepath 
                        os.remove(filepath)
                        exit
                    #else:
                        #print "diff is NOT None"
    
                    #print "-------"
                    
            continue
    continue
print("########################")
    

#name1 = "1-1.png"
#name2 = "1-2.png"

#a = cv2.imread("1-1.png")
#b = cv2.imread("1-2.png")

#diff = cv2.subtract(a, b)    

#print diff

#if diff is None:
#    print "diff is None"
#    #os.remove("/Users/pranaysadarangani/eclipse-workspace/dup/src/1-2.png")
#    filepath = os.path.join(dirpath,name2)
#    print filepath 
#    os.remove(filepath)
#else:
#    print "diff is NOT None"



