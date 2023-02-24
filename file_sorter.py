import os, shutil

# Path to files that need to be sorted
path = os.getcwd()
path += "\\File_Sorter\\Files\\"

# Pull in files from the selected folder and determines if a folder is needed and sorts them accordingly
for file in os.listdir(path):
    ext_index = (file.index('.'))
    ext = file[ext_index:]
    if not os.path.exists(f'{path}\\{ext[1:]}_files\\'):
        os.makedirs(f'{path}\\{ext[1:]}_files\\')

    # Move files to the correct folder
    shutil.move(f'{path}\\{file}', f'{path}\\{ext[1:]}_files\\')
