
import shutil
import os
from_dir="C:/Users/vishal/Downloads"
to_dir="C:/Users/vishal/Desktop/New folder (5)"
list_of_file=os.listdir(from_dir)
#print(list_of_file)
for f in list_of_file:
    name,extension=os.path.splitext(f)
    if extension=='':
        continue 
    if extension in ['.gif','.png','.jpg','.jpeg',',jfif']:
        path1=from_dir+'/'+f
        path2=to_dir+'/'+"imagefile"
        path3=to_dir+'/'+"imagefile"+'/'+f
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)
            



















