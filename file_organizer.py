import os

try:
    #make list that only contains files
    path = input("enter your path : ")
    items = os.listdir(path)
    items_path = []
    for item in items:
        item_path = os.path.join(path, item)
        items_path.append(item_path)
    files_path = [file_path for file_path in items_path if os.path.isfile(file_path)]

    #organize files
    for file_path in files_path:
        ext = os.path.splitext(file_path)[1] #get extension
        folder = os.path.join(path, ext[1:])
        destination = os.path.join(folder, os.path.basename(file_path))

        #check if folder is already exits
        if os.path.exists(folder):
            if os.path.exists(destination):
                print(os.path.basename(destination)+"is already there")
            else:
                os.replace(file_path, destination)

        #if is not exits make it
        else:
            os.makedirs(folder)
            os.replace(file_path, destination)

except:
    print("program failed")