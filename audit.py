import requests
from pprint import pprint
from ff_config import ff_config

api_url = "https://app.launchdarkly.com/api/v2/"
params_flags = api_url + "flags/{0}?env={1}"

#url = "https://app.launchdarkly.com/api/v2/flags/" + proj_key + "?env=" + env_key
#url = "https://app.launchdarkly.com/api/v2/flag-statuses/" + proj_key + "/" + env_key


def main():
    config = ff_config()
    headers = {"Authorization": config.api_token}
    url = params_flags.format(config.project_key, config.environment_key)
    response = requests.get(url, headers=headers)

    data = response.json()
    pprint(data)


if __name__ == "__main__":
    main()