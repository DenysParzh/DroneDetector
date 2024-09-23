import json

from googleapiclient import discovery

from .icomand import IComand
from .query_settings import QuerySettings


class YouTubeSearcher(IComand):
    def __init__(self, api_key: str, query_settings: QuerySettings, output_json_path: str):
        self.api_key = api_key
        self.youtube_service = discovery.build(serviceName='youtube',
                                               version='v3',
                                               developerKey=api_key)
        self.query_settings = query_settings
        self.output_json_path = output_json_path

    def execute(self):
        response = self._search_video_metadata(self.query_settings)
        response = self._response_parser(response)
        self._download_data(response)
        return response

    def _search_video_metadata(self, settings: QuerySettings) -> list:
        print(settings.get_query_string())

        response = (self.youtube_service
                    .search()
                    .list(q=settings.get_query_string(),
                          part=settings.part,
                          maxResults=settings.max_count,
                          publishedAfter=settings.published_after,
                          publishedBefore=settings.published_before,
                          regionCode=settings.region_code)
                    .execute())

        return response['items']

    @staticmethod
    def _response_parser(response: list) -> list:
        domain = "https://www.youtube.com"
        path_list = []

        for item in response:
            if item['id']['kind'] == 'youtube#video':
                video_title = item['snippet']['title']
                video_url = f"{domain}/watch?v={item['id']['videoId']}"
                path_list.append({'title': video_title, 'url': video_url, "mark": 0})

        return path_list

    def _download_data(self, data: list):
        with open(self.output_json_path, 'w', encoding='utf-8') as stream:
            json.dump(data, stream, indent=2, ensure_ascii=False)
