import os

# Get the current working directory
print(os.getcwd())

# Change directory
# os.chdir('../Pygame')

# Get the current working directory
print(os.getcwd())

# Create a folder in current directory
# One level
os.chdir("newDir")

# Depth
# os.makedirs('test/test1/test2')

# os.rename('test1', 'test2')

# Get the current working directory
print(os.getcwd())

# print(os.path.isfile(''))
#
# print(os.path.isdir(''))

# Delete directory at path
os.rmdir('')
os.re
os.chdir('')
print(os.getcwd())

os.removedirs("") #CAUTION

# rename a file
# os.rename("", "") # (current filename, new filename)

# Lets you walk a path

for dirpath, dirnames, filenames in os.walk('ENTER DIRECTORY'):
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Filenames:", filenames, "\n")

# Get file Size
# print(os.stat(".txt").st_size) # in bytes