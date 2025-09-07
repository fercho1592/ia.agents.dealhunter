from infrastructure.config_reader.YamlConfigService import YamlConfigService


def main():
    config_service = YamlConfigService()

    print("Service API Keys:")
    for service in config_service.get_all_services():
        print(f" - {service}: {config_service.get_service_api_key(service)}")

    print("Welcome to my Python console application!")

if __name__ == "__main__":
    main()