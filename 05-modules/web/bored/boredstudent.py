import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning


try:
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    url = 'https://www.boredapi.com/api/activity'
    request = requests.get(url, verify=False)
    json_data = json.loads(request.text)
    print(str(json_data['activity']).strip())
except requests.exceptions.SSLError:
    pass