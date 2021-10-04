import requests
import csv
import os
import os.path
from datetime import datetime
from ff_config import ff_config


class ff_data(object):
    __api_url = "https://app.launchdarkly.com/api/v2/"
    __params_flags = __api_url + "flags/{0}?env={1}"
    __params_flag_status = __api_url + "flag-statuses/{0}/{1}/{2}"

    __csv_column = ["Key", "Environment", "On", "Last modified (days)", "Last evaluated (days)", "Created", "Updated", "Owner", "Description", "Tags"]

    __config = ff_config()


    def __api_request(self, url):
        headers = {"Authorization": self.__config.api_token}
        response = requests.get(url, headers=headers)
        if response.ok:
            return response.json()
        else:
            response.raise_for_status()


    def __create_folder(self, path):
        if not os.path.exists(path):
            os.makedirs(path)


    def __create_csv(self, rows):
        today = datetime.now()
        path = ".//data//"
        self.__create_folder(path)

        filename = "{0}//feature-flags-{1:%Y-%m-%d}.csv".format(path, today)
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(self.__csv_column)
            writer.writerows(rows)

        print("Extracted {0} feature flags to \"{1}\"".format(len(rows), filename))

        return filename


    def __get_date_from_utc_string(self, date):
        if date:
            # 2020-02-05T18:17:01.514Z
            return datetime.strptime(date.split(".")[0], "%Y-%m-%dT%H:%M:%S")


    def __get_date_from_milliseconds(self, milliseconds):
        return datetime.fromtimestamp(milliseconds / 1000.0)


    def __get_last_evaluated(self, flag_key, environment):
        url = self.__params_flag_status.format(self.__config.project_key, environment, flag_key)
        data = self.__api_request(url)
        return data["lastRequested"]


    def __get_team_name(self, email):
        return email.split("@")[0]
        

    # https://apidocs.launchdarkly.com/tag/Feature-flags#section/Sample-feature-flag-representation
    def __store_feature_flag_data(self, flags, rows, environment):
        for flag in flags:
            key = flag["key"]
            description = flag["description"]
            tags = flag["tags"]
            owner = self.__get_team_name(flag["_maintainer"]["email"])
            active = flag["environments"][environment]["on"]
            created_date = self.__get_date_from_milliseconds(flag["creationDate"])
            updated_date = self.__get_date_from_milliseconds(flag["environments"][environment]["lastModified"])

            last_requested = self.__get_last_evaluated(key, environment)

            days_since_update = (datetime.now() - updated_date).days
            days_last_evaluated = ""
            if last_requested:
                request_date = self.__get_date_from_utc_string(last_requested)
                if request_date:
                    days_last_evaluated = (datetime.now() - request_date).days

            rows.append([key, environment, active, days_since_update, days_last_evaluated, created_date.strftime('%d/%m/%y'), updated_date.strftime('%d/%m/%y'), owner, description, tags])


    def __get_feature_flags(self, environment):
        url = self.__params_flags.format(self.__config.project_key, environment)
        data = self.__api_request(url)
        return data["items"]


    def extract_audit_data(self):
        csv_rows = []

        for env_key in self.__config.environment_keys:
            environment = env_key.strip()
            print("Processing \"{0}\" ...".format(environment))
            data = self.__get_feature_flags(environment)
            self.__store_feature_flag_data(data, csv_rows, environment)

        self.__create_csv(csv_rows)