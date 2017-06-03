import os

def rename_files():
    # translation table
    numbers = "1234567890"
    spaces = "asdfghjkl;"
    transtab = str.maketrans(numbers,spaces)

    test = "123tyu"
    test = test.translate(transtab)
    print(test)

    path = os.getcwd()
    print(path);

    # change to the directory with the images
    os.chdir("prank")

    path = os.getcwd()
    print(path);
    
    # get file names from a folder
    file_list = os.listdir(r"/Users/Michael/Development/Udacity/Python/prank")
    # for every file
    for file in file_list:
        # rename it removing all numbers
        os.rename(file,file.translate(file.maketrans('','','1234567890')))
        print(file)

rename_files()
