import os
from dotenv import load_dotenv
from src.query_settings import QuerySettings
from src.youtube_service_fabric import YoutubeServiceFabric

load_dotenv()


def main():
    api_key = os.getenv('API_KEY')
    settings = QuerySettings(query=["Ланцет-1 БПЛА"],
                             max_count=10,
                             region_code="RU")

    threads = 4
    json_path = "./output_json.json"
    download_path = "./data"
    type = "download"

    service = YoutubeServiceFabric(api_key, settings, json_path, download_path, threads).build(type)
    service.execute()


if __name__ == '__main__':
    main()
