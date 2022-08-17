from zipfile import ZipFile
with ZipFile('moetZip.zip','r') as zip:
    listofeils = zip.namelist()

for i in listofeils:
    print(i)