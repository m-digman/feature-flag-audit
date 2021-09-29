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
            self.__project_key = ff_config[0]["launchdarkly"]["project"]
            self.__environment_key = ff_config[0]["launchdarkly"]["environment"]


    @property
    def api_token(self):
        return self.__api_token


    @property
    def project_key(self):
        return self.__project_key


    @property
    def environment_key(self):
        return self.__environment_key