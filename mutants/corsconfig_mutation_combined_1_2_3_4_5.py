class CORSConfig:
    ORIGINS = ['http://example.com', 'http://another-example.com']
    METHODS = ['*']
    ALLOW_HEADERS = ['*']
    SUPPORTS_CREDENTIALS = True
    MAX_AGE = 86400
    SEND_WILDCARD = True
    AUTOMATIC_OPTIONS = False
    VARY_HEADER = True


class AppConfig:
    API_KEY = 'your_secret_api_key'
