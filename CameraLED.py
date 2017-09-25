import requests
import requests.auth
import logging


class CameraLED:
    def __init__(self, ip_address, username, password):
        self._ip_address = ip_address
        self._username = username
        self._password = password
        self._status = None

    @property
    def enabled(self):
        return self._status

    @enabled.setter
    def enabled(self, value):
        self._status = value
        state_string = 'auto' if value else 'close'
        url = 'http://' + self._ip_address + '/hy-cgi/irctrl.cgi?cmd=setinfrared&infraredstatus=' + state_string
        response = requests.get(url, auth=requests.auth.HTTPDigestAuth(self._username, self._password))
        if not response.ok:
            logging.error('Could not authenticate with IP camera!')
            raise RuntimeError('Could not authenticate with IP camera!')
