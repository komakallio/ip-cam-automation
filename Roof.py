import requests
import logging


class Roof:
    def __init__(self, ip_address, port):
        self._ip_address = ip_address
        self._port = port

    @property
    def open(self):
        url = 'http://' + self._ip_address + ':' + str(self._port) + '/api/roof'
        response = requests.get(url)
        if not response.ok:
            logging.warning('Could not retrieve roof state!')
            raise RuntimeError('Roof status not available!')
        roof_state = response.json()['Roof']['State']
        return roof_state == 'OPEN'
