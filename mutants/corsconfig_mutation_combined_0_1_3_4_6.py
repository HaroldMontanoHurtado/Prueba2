class CORSConfig:
    ORIGINS = ['*']
    METHODS = ['*']
    ALLOW_HEADERS = ['Authorization', 'Content-Type']
    SUPPORTS_CREDENTIALS = True
    MAX_AGE = 86400
    SEND_WILDCARD = False
    AUTOMATIC_OPTIONS = True
    VARY_HEADER = True


class AppConfig:
    API_KEY = 'your_secret_api_key'