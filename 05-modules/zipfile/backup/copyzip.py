import os
import zipfile
import sys
naamDirectory = os.path.basename(sys.argv[1])

zf = zipfile.ZipFile(f"{sys.argv[2]}/{os.path.basename(sys.argv[1])}.zip", "w")
for dirname, subdirs, files in os.walk(str(sys.argv[1])):

    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()