import urllib.parse
import base64
import hashlib
import json
import requests
import time


class IntranetClient:
    def __init__(self, key: str, secret: str, url: str):
        self.key = key
        self.secret = secret
        self.url = url

    def get_student_projects(self, student_id):
        return self.get('students/{}/projects'.format(student_id))

    def get_student(self, student_id):
        return self.get('students/{}'.format(student_id))

    def get_list(self, path, cursor=None):
        result = self.get(path, cursor)
        items = result['items']
        if result['next'] is not None:
            items += self.get_list(path, result['next'])

        return items

    def get(self, path, cursor=None):
        url = self.url + path
        credentials = {'key': self.key, 'secret': self.secret}
        timestamp = int(time.time())

        query_string = {'timestamp': timestamp}
        if cursor is not None:
            query_string['cursor'] = cursor

        request = {'method': 'GET', 'params': query_string, 'path': '/api/v1/' + path, 'raw_body': None}

        signature_components = ["{}={}&".format(k, request['params'][k]) for k in sorted(request['params'].keys())]
        if request['raw_body'] is not None:
            signature_components.append(json.dumps(request['raw_body']))

        signature_components.append(request['method'])
        signature_components.append(request['path'])
        signature_components.append(credentials['secret'])

        signature = hashlib.sha1(''.join(signature_components).encode()).hexdigest().lower()
        token = base64.b64encode("{}:{}".format(credentials['key'], signature).encode('utf8')).decode('utf8')

        headers = {'HBTN_TOKEN': token, 'Content-Type': 'application/json', 'Accept': 'application/json'}
        result = None
        trial = 0
        while result is None and trial < 3:
            try:
                return requests.get(url, params=urllib.parse.urlencode(request['params'], True, safe="="),
                                    headers=headers).json()
            except:  # try smaller except (even ctrl-c is now caught!)
                trial = trial + 1
                print("Something went wrong: {}".format(trial))
