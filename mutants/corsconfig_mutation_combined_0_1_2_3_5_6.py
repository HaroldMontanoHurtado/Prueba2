class CORSConfig:
    ORIGINS = ['*']
    METHODS = ['*']
    ALLOW_HEADERS = ['*']
    SUPPORTS_CREDENTIALS = True
    MAX_AGE = 3600
    SEND_WILDCARD = True
    AUTOMATIC_OPTIONS = True
    VARY_HEADER = True


class AppConfig:
    API_KEY = 'your_secret_api_key'
