import os
import re

def dup_format(n):
    pattern = r'^.+\s+\(\d+\).{0,6}$'
    return bool(re.match(pattern, n))


root = input("Input root directory to search\n")

target_files = []

for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if dup_format(filename):
            target_files.append(os.path.join(dirpath, filename))

#format files to be deleted
print("\n")
for file in target_files:
    print(f"{file}")

confirm = input("\n The above files will be deleted. Enter CONFIRM if you wish to proceed.\n")
if confirm == 'CONFIRM':
    for file in target_files:
        os.remove(file)
    print("Duplicates successfully removed.")
else:
    print("Deletion cancelled.")
