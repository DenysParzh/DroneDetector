from .youtube_downloader import YouTubeVideoDownloader
from .youtube_searcher import YouTubeSearcher


class YoutubeServiceFabric:
    def __init__(self, api_key, settings, json_path, download_path, threads):
        self.threads = threads
        self.settings = settings
        self.json_path = json_path
        self.download_path = download_path
        self.api_key = api_key

    def build(self, type: str):
        match type:
            case 'download':
                return YouTubeVideoDownloader(json_path=self.json_path,
                                              download_path=self.download_path,
                                              threads=self.threads)
            case 'search':
                return YouTubeSearcher(api_key=self.api_key,
                                       query_settings=self.settings,
                                       output_json_path=self.json_path)
