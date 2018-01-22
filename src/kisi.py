import requests
import json


class Kisi(object):

    def __init__(self, config):
        self.__email  = config['kisi_email']
        self.__pwd    = config['kisi_password']
        self.__door   = config['kisi_door_id']

    def __authenticate(self):
        headers = {
            'Accept':       'application/json',
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            'user': {
                'email':    self.__email,
                'password': self.__pwd
            }
        })
        result = requests.post(
            'https://api.getkisi.com/users/sign_in',
            headers = headers, 
            data    = payload
        )
        self.__secret = result.json()['secret']

    def __unlock_door(self):
        headers = {
            'Accept':        'application/json',
            'Content-Type':  'application/json',
            'X-Login-Secret': self.__secret
        }
        requests.post(
            'https://api.getkisi.com/locks/{}/unlock'.format(self.__door),
            headers = headers
        )

    def unlock(self):
        try:
            self.__authenticate()
            self.__unlock_door()
            print('  Door unlocked')
        except ConnectionError:
            print('  Connection error')
        self.__secret = ''

