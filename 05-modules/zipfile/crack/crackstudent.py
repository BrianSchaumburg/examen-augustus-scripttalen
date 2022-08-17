from itertools import product
import zipfile
from string import ascii_lowercase
keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 4)]

zip_file = zipfile.ZipFile('crack (1).zip')
for keyword in keywords:
    try:
        zip_file.extractall(pwd=str.encode(keyword))
        print("password found: " + keyword)
    except:
        continue


