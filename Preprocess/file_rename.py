import os

start_num = 632
for filename in os.listdir():
    if '.py' in filename:
        continue
    os.rename(filename, str(start_num)+'.jpg')
    start_num += 1
