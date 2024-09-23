import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pytubefix import YouTube
from .icomand import IComand


class YouTubeVideoDownloader(IComand):
    def __init__(self, json_path, download_path, threads):
        self.json_path = json_path
        self.download_path = download_path
        self.threads = threads

    def execute(self):
        data = self._load_json_data()
        data = self._filter(data)
        self._download(data)

    def _load_json_data(self) -> list:
        with open(self.json_path, 'r', encoding='utf-8') as json_stream:
            output = json.load(json_stream)

        return output

    def _download(self, data: list[str]):
        def _download_helper(video_path):
            try:
                yt = YouTube(video_path)
                (yt.streams.filter(res="1080p", mime_type="video/mp4", only_video=True)
                 .first()
                 .download(self.download_path))

            except Exception as e:
                print(f"Failed to download {video_path}. Reason: {e}")

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = [executor.submit(_download_helper, video_path) for video_path in data]

            for future in as_completed(futures):
                future.result()


    @staticmethod
    def _filter(data: list[dict]) -> list[str]:
        return [video["url"] for video in data if bool(video["mark"])]
