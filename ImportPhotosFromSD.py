# emily rexer
# 03/22/20

# notes:
    # requires consistent date format for labeling folders
    # removes files from SD card

from datetime import datetime
import os
import shutil


def ImportPhoto(importPath, exportPath):

    importDirectory = os.fsencode(importPath)
    exportDirectory = os.fsencode(exportPath)

    # go through all photos
    for photo in os.listdir(importDirectory):
        photoname = os.fsdecode(photo)
        photoPath = importPath + '/' + photoname

        # get date photo was created
        photoDate = datetime.fromtimestamp(os.path.getmtime(photoPath)).strftime('%Y-%m-%d')
        print(photoDate)

        # folder where photo will be moved
        photoExportFolderPath = exportPath +'/' + photoDate

        # new path for photo
        photoExportPath = photoExportFolderPath + '/' + photoname

        # if no folder with matching date, create folder
        if not os.path.exists(photoExportFolderPath):
            os.mkdir(photoExportFolderPath)
            print('CREATED DIRECTORY')

        # move photo into correct folder
        shutil.move(photoPath, photoExportPath)

ImportPhoto('/mnt/e/DCIM/100CANON', '/mnt/c/Users/erexer/Pictures/2020')
