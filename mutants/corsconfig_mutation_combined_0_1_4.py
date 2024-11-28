class CORSConfig:
    ORIGINS = ['*']
    METHODS = ['*']
    ALLOW_HEADERS = ['Authorization', 'Content-Type']
    SUPPORTS_CREDENTIALS = False
    MAX_AGE = 86400
    SEND_WILDCARD = False
    AUTOMATIC_OPTIONS = False
    VARY_HEADER = True


class AppConfig:
    API_KEY = 'your_secret_api_key'