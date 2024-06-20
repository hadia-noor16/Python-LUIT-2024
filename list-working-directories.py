import os
path='.'
files = os.listdir(path)
list=[]
for f in files:
    #print(f)
    file_info = os.stat(f)
    size = file_info.st_size
    #print(f"File: {f}, Size: {size} bytes")
    #filenames[f]=size
    filenames={'File':f, 'Size': size}
    list.append(filenames)
#print(filenames)
    
print(list)


