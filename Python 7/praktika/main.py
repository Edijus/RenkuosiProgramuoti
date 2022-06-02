# Task 5
import os
import datetime

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
new_dir = os.path.join(desktop, 'Naujas Katalogas')
if not os.path.exists(new_dir):
  os.mkdir(new_dir)

file_path = os.path.join(new_dir, 'new_file.txt')
with open(file_path, 'w') as f:
    f.write(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

file_creation_time = os.path.getctime(file_path)
dt_c = datetime.datetime.fromtimestamp(file_creation_time)
print('Created on:', dt_c)

file_stats = os.stat(file_path)
print(f'File Size in Bytes is {file_stats.st_size}')
