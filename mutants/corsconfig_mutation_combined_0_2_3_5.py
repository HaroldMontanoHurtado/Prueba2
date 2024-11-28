class CORSConfig:
    ORIGINS = ['*']
    METHODS = ['GET', 'POST', 'PUT', 'DELETE']
    ALLOW_HEADERS = ['*']
    SUPPORTS_CREDENTIALS = True
    MAX_AGE = 3600
    SEND_WILDCARD = True
    AUTOMATIC_OPTIONS = False
    VARY_HEADER = True


class AppConfig:
    API_KEY = 'your_secret_api_key'
