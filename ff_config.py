import yaml

class ff_config(object):
    __ff_config_file = "ff_config.yaml"


    def __init__(self, config_file = None):
        if config_file:
            self.__ff_config_file = config_file
        self.__load_config()


    def __load_config(self):
        with open(self.__ff_config_file, "r") as config_file:
            ff_config = yaml.safe_load(config_file)
            self.__api_token = ff_config[0]["launchdarkly"]["token"]


    @property
    def api_token(self):
        return self.__api_token