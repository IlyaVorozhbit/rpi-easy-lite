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

def read_animation(id):
    config.read('anims/' + id + '.ini')

    print(config['anim_config']['frames_count'])
    print(config['anim_config']['frame_length'])
    print(config['anim_frame_1']['red'])
    return config

    print('anims/' + id + '.ini')

def write_config():
    with open(settings_name, 'w') as configfile:
        config.write(configfile)

# read_config()
# print(config['colors']['red'])
