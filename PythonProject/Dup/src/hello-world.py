print("Goodbye, World!")

import cv2

import os

import sys

import numpy as np

dirpath = os.getcwd()
#print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
#print("Directory name is : " + foldername)

dirpath = dirpath + "/src"


for filename1 in os.listdir(dirpath):
    if filename1.endswith(".DS_Store") or filename1.endswith(".py"): 
        # print(os.path.join(directory, filename))
        continue
    else:
        for filename2 in os.listdir(dirpath):
            if filename2.endswith(".DS_Store") or filename2.endswith(".py"): 
                # print(os.path.join(directory, filename))
                continue
            else:
                if filename1!=filename2:
                    
                    print filename1
                    print filename2
                    
                    filepath1 = os.path.join(dirpath,filename1)
                    filepath2 = os.path.join(dirpath,filename2)
                    
                    a = cv2.imread(filepath1)
                    b = cv2.imread(filepath2)
                    
                    height1, width1, channels1 = a.shape
                    #print height, width, channels
                    
                    height2, width2, channels2 = b.shape
                    #print height, width, channels
                    
                    b1,g1,r1 = cv2.split(a)
                    b2,g2,r2 = cv2.split(b)
                    
                    pxa1 = a[1,1]
                    pxb1 = b[1,1]
                    
                    bEqual = True;
                    
                    if height1 != height2: 
                        bEqual = False;
                    if width1 != width2: 
                        bEqual = False;
                    if channels1 != channels2: 
                        bEqual = False;
                    if a.dtype != b.dtype:
                        bEqual = False;
                    if a.size != b.size:
                        bEqual = False;
                    if b1.all() != b2.all():
                        bEqual = False;
                    if g2.all() != g2.all():
                        bEqual = False;
                    if r1.all() != r2.all():
                        bEqual = False;
                                
                    for row in range(0, 100):
                        for col in range(0, 100): 
                            if a[row,col].all() != b[row,col].all():
                                bEqual = False;
                    
                    
                    #print a
                    #print b
                    
                    #diffab = cv2.subtract(a, b)
                    #diffba = cv2.subtract(b, a)
                    
                    #if difference is all zeros it will return False
                    #result = not np.any(diffab)
                    
                    #print result
                    
                    #diffba = cv2.absdiff(a, b)
                    
                    #diff = cv2.compare(a,b)
                    
                    #b, g, r = cv2.split(diff)
                    
                    #print diffab
                    #print diffba
                    
                    
                    #if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                    #    print("The images are completely Equal")
        
                    if bEqual is True:
                        #print "diff is None"
                        #os.remove("/Users/pranaysadarangani/eclipse-workspace/dup/src/1-2.png")
                        #filepath2 = os.path.join(dirpath,filename2)
                        
                        print filepath1
                        print filepath2 
                        os.remove(filepath2)
                        
                        print "################"
                        
                        sys.exit()
                        
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



