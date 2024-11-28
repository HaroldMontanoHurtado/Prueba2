class CORSConfig:
    ORIGINS = ['*']
    METHODS = ['*']
    ALLOW_HEADERS = ['Authorization', 'Content-Type']
    SUPPORTS_CREDENTIALS = True
    MAX_AGE = 3600
    SEND_WILDCARD = False
    AUTOMATIC_OPTIONS = False
    VARY_HEADER = False


class AppConfig:
    API_KEY = 'your_secret_api_key'
