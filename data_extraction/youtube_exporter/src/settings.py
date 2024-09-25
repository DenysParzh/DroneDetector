import json
import os

from .query_settings import QuerySettings


class JsonSettings:
    def __init__(self, json_setting_path):
        self.json_setting_path = json_setting_path
        self.data_folder = "./data"
        self.settings = self._create_template()
        self._read()
        self._convert()

    def _read(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

        if not os.path.exists(self.json_setting_path):
            with open(self.json_setting_path, 'w', encoding='utf-8') as stream:
                json.dump(self.settings, stream, indent=2, ensure_ascii=False)
        else:
            with open(self.json_setting_path, 'r', encoding='utf-8') as stream:
                self.settings = json.load(stream)

    def _convert(self):
        json_raw_settings = self.settings["query_settings"]
        self.query = QuerySettings(query=json_raw_settings["query"],
                                   exclude=json_raw_settings["exclude"],
                                   max_count=json_raw_settings["max_count"],
                                   region_code=json_raw_settings["region_code"],
                                   published_after=json_raw_settings["published_after"],
                                   published_before=json_raw_settings["published_before"], )

        self.type = self.settings["type"]
        self.json_path = self.settings["json_path"]
        self.download_path = self.settings["download_folder_path"]
        self.threads = self.settings["max_threads"]
        self.api_key = self.settings["api_key"]

    @staticmethod
    def _create_template():
        template = {
            "type": "search",
            "query_settings": {
                "query": [],
                "exclude": [],
                "max_count": 10,
                "region_code": "UA",
                "published_after": {"year": 2000, "month": 1, "day": 1},
                "published_before": {"year": 2030, "month": 1, "day": 1}
            },
            "json_path": "./data/video_paths.json",
            "download_folder_path": "./data/video",
            "max_threads": 4,
            "api_key": "",
        }

        return template
