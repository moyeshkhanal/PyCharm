import os

# Get current working directory
print(os.getcwd())

# Change directory
os.chdir('/Users/mkhanal/PycharmProjects/Pygame') # Must be a path string that you pass in

print(os.getcwd())

# List directory/files in the current directory
print(os.listdir())

# Create a folder in the directory
# One level
os.mkdir("Test")
#
# # Allows depth
# os.makedirs("Test")
#
# # If path is a valid directory or not
# os.path.isdir()
#
# # is path is a file
# os.path.isfile()
#
# # Delete folder
# # One level same as mkdir, use this to be safer
# os.rmdir()
#
# # Depth like mkdirs
# os.removedirs()
#
# # Rename a file
# os.rename() # (name of current file, new file name)
#
# # Get the size of a file
# os.stat("momoney.txt").st_size()
#
# # Lets you walk the directories
# os.walk("Directory Path") # Pass in the directory to walk
# # Returns a tuple with 3 values, Directory Path, Directory Names, and File names
#
# for dirpath, dirnames, filenames in os.walk('/Users/mkhanal/PycharmProjects/OsModule'):
#     print("Current Path:", dirpath)
#     print("Directories:", dirnames)
#     print("Filenames:", filenames, "\n")