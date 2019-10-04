import os
from PIL import Image as Pimg

def nameChange():
    files = os.listdir()
    for i in files:
         if ".jpg" in i:
             img = Pimg.open(i)
             exifData = img._getexif()
             os.rename(i,exifData[36868])
#changes the ":" character in the names of the files so the are valid
def editName():
    file_list = os.listdir()

    for _file in file_list:
        tempWord = []
        for f in _file:
            if f == ":":
                tempWord.append("_")
            else:
                tempWord.append(f)
        newName = "".join(tempWord)
        os.rename(_file,newName)

if __name__ == "__main__":
    nameChange()
    editName()