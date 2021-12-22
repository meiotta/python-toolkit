import shutil
import os

# the folder you want to empty
dir= "YOUR DIRECTORY"

#cycle thru the directory, delete file if it's a file or folder if it's not
for f in os.listdir(dir):
    file_path = os.path.join(dir,f)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('failed to delete for some reason, and that reason is you %s   Reason' %(file_path, e) )
