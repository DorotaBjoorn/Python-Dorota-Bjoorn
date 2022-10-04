import sys, os

print(os.path.dirname(__file__))    #letar fram denna filens (main) directory name (example3_paths)

root_path = os.path.dirname(__file__)
path_folder1 = os.path.join(root_path, "folder1")
path_folder2 = os.path.join(root_path, "folder2")

os.system("cls||clear")
print("="*100)

print(root_path)

print()

print(path_folder1)

print("="*100)

sys.path.append(path_folder1)       #sys.path är en lista av alla sökvägar som Python letar bland och där har vi lagt till folder1 och 2
sys.path.append(path_folder2)       #behövs för att kunna importera module1 och module2 (testa print(sys.path))

import module1, module2

# print(sys.path)





#print(os.path.dirname(__file__))    #letar fram denna filens (main) directory name (example3_paths)
# import module2 funkar inte direkt eftersom den inte ligger i samma mapp som main