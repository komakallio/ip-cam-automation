import configparser
import os
import time
import logging
from CameraLED import CameraLED
from Roof import Roof


def main():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    # Configure logger
    log_file = os.path.join(base_dir, 'cam-automation.log')
    logging.Formatter.converter = time.gmtime
    logging.basicConfig(filename=log_file, format='%(asctime)s - %(name)s:%(levelname)s - %(message)s')

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
        led.enabled = not roof.open
        time.sleep(polling_interval)


if __name__ == '__main__':
    main()
