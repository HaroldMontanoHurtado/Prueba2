class CORSConfig:
    ORIGINS = ['*']
    METHODS = ['*']
    ALLOW_HEADERS = ['*']
    SUPPORTS_CREDENTIALS = True
    MAX_AGE = 86400
    SEND_WILDCARD = True
    AUTOMATIC_OPTIONS = True
    VARY_HEADER = False


class AppConfig:
    API_KEY = 'your_secret_api_key'