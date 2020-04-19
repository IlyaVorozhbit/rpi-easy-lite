import configparser

settings_name = 'config.ini'
config = configparser.ConfigParser()

def init_default_config():
    config['colors'] = {}
    config['colors']['red'] = "255"
    config['colors']['green'] = "255"
    config['colors']['blue'] = "255"

def read_config():
    init_default_config()
    config.read(settings_name)

def write_config():
    with open(settings_name, 'w') as configfile:
        config.write(configfile)

# read_config()
# print(config['colors']['red'])
