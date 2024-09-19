import os
from dotenv import load_dotenv
from youtube_exporter import YouTubeExporter

load_dotenv()


def main():
    api_key = os.getenv('API_KEY')
    query_setting = {
        'query': ["Wing drone", "XWing drone"],
        'part': "id,snippet",
        'max_results': 30
    }

    service = YouTubeExporter(api_key)
    response = service.search(query_setting)

    print(response)


if __name__ == '__main__':
    main()
