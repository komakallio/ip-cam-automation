import configparser
from CameraLED import *
from Roof import *


def main():
    logging.basicConfig(filename='cam-automation.log', format='%(asctime)s - %(message)s')

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

    logging.debug('Setting LED status')
    led.enabled = roof.closed


if __name__ == '__main__':
    main()
