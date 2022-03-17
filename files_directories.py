

from pathlib import Path
# ----
# Absolute path = root directory
# Relative path = current project directory

# Create a path object
path = Path("/Users/nct/Dropbox/ComputerScience/PythonCourse2/ecommerce2")
# ---------------------------------------

print(f"\n\npath = {path}") #print the path
# ---------------------------------------

print(f"path.exists() =  + {path.exists()})") #boolean - check if path exists
# ---------------------------------------
print("\n\nCreate new folder")
newPath = Path("/Users/nct/Dropbox/ComputerScience/PythonCourse2/ecommerce2/fromFiles_directories_dotpy")
if newPath.exists():
    print("Path already exists.")
else:
    newPath.mkdir()
# ---------------------------------------

print("Now remove the directory")
if newPath.exists():
    newPath.rmdir()
else:
    print("Path already exists.")
# ---------------------------------------

print("\n\nPrint all files in the directory")
newestPath = Path("/Users/nct/Dropbox/ComputerScience/PythonCourse2/ecommerce2/")
for file in path.glob('*.*'): # print all files
    print(file)
    # ----------------
print("\n\nPrint all .py files in the directory")
for file in path.glob('*.py'): # print all PYTHON files
    print(file)