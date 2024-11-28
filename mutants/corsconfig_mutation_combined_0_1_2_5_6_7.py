class CORSConfig:
    ORIGINS = ['*']
    METHODS = ['*']
    ALLOW_HEADERS = ['*']
    SUPPORTS_CREDENTIALS = False
    MAX_AGE = 3600
    SEND_WILDCARD = True
    AUTOMATIC_OPTIONS = True
    VARY_HEADER = False


class AppConfig:
    API_KEY = 'your_secret_api_key'
