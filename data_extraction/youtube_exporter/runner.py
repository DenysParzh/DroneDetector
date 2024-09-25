from src.settings import JsonSettings
from src.youtube_service_fabric import YoutubeServiceFabric


def main():
    setting_path = "./data/settings.json"
    settings = JsonSettings(setting_path)

    service = YoutubeServiceFabric(settings.api_key,
                                   settings.query,
                                   settings.json_path,
                                   settings.download_path,
                                   settings.threads).build(settings.type)
    service.execute()


if __name__ == '__main__':
    main()
