myDict = {
    "py": "Python",
    "txt": "Text",
    "docs": "Document",
    "xls": "Excel",
    "ppt": "Power Point",
}

filename = input("Input the filename: ")
file_ext = filename.split('.')
file_ext1 = file_ext[1]

print("The extension of the file is : ", myDict.get(file_ext1))
