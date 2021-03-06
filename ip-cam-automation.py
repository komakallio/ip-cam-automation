import configparser
import time
import logging
from CameraLED import CameraLED
from Roof import Roof


def main():
    # Configure logger
    logging.Formatter.converter = time.gmtime
    logging.basicConfig(format='%(asctime)s - %(name)s:%(levelname)s - %(message)s')

    logging.debug('Reading config file.')
    config = configparser.ConfigParser()
    config.read('config.ini')

    ip_cam_username = config['IPCam']['Username']
    ip_cam_password = config['IPCam']['Password']
    ip_cam_ip_address = config['IPCam']['IP']
    led = CameraLED(ip_cam_ip_address, ip_cam_username, ip_cam_password)

    roof_ip_address = config['Roof']['IP']
    roof_port = config['Roof']['Port']
    roof = Roof(roof_ip_address, roof_port)

    polling_interval = int(config['General']['PollingIntervalSeconds'])

    while True:
        logging.debug('Setting LED status')
        try:
            led.enabled = not roof.open
        except KeyError:
            logging.error('Invalid response from API', exc_info=True)
        except RuntimeError:
            logging.error('Runtime error', exc_info=True)
        finally:
            time.sleep(polling_interval)


if __name__ == '__main__':
    main()
