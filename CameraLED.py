import logging
import requests
import requests.auth


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
        try:
            response = requests.get(url, auth=requests.auth.HTTPDigestAuth(self._username, self._password))
            if not response.ok:
                logging.warning('Could not authenticate with IP camera!')
                raise RuntimeError('Could not authenticate with IP camera!')
        except Exception:
            logging.warning('Could not connect to IP camera!', exc_info=True)
            raise RuntimeError('Could not connect to IP camera!')
