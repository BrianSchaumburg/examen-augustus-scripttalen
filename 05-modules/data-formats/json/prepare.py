
import urllib.request
from zipfile import ZipFile


urllib.request.urlretrieve('http://scripting.leone.ucll.be/data/covid.zip', 'ageplot/covid.zip')


with ZipFile('ageplot/covid.zip') as file:
    file.extract('covid.json')
