import requests
from pprint import pprint
from ff_config import ff_config

proj_key = "default"
env_key = "prod"
#url = "https://app.launchdarkly.com/api/v2/flags/" + proj_key
url = "https://app.launchdarkly.com/api/v2/flags/" + proj_key + "?env=" + env_key
#url = "https://app.launchdarkly.com/api/v2/flag-statuses/" + proj_key + "/" + env_key


def main():
    config = ff_config()
    headers = {"Authorization": config.api_token}
    response = requests.get(url, headers=headers)

    data = response.json()
    pprint(data)


if __name__ == "__main__":
    main()