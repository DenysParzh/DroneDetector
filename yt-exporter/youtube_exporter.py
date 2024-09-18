from googleapiclient import discovery


class YouTubeExporter:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.youtube_service = discovery.build(serviceName='youtube',
                                               version='v3',
                                               developerKey=api_key)

    def search(self, query_settings: dict):
        response = self._search_video_metadata(query_settings)
        response = self._response_parser(response)
        return response

    @staticmethod
    def _response_parser(response: list):
        path_list = []

        for item in response:
            if item['id']['kind'] == 'youtube#video':
                video_title = item['snippet']['title']
                video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
                path_list.append({'title': video_title, 'url': video_url})

        return path_list

    def _search_video_metadata(self, query_settings: dict):
        queries = query_settings['query']

        if isinstance(queries, str):
            queries = [queries]

        all_responses = []
        for query in queries:
            response = (self.youtube_service
                        .search()
                        .list(q=query,
                              part=query_settings['part'],
                              maxResults=query_settings['max_results'])
                        .execute())

            all_responses.extend(response['items'])

        return all_responses
