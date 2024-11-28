class CORSConfig:
    ORIGINS = ['http://example.com', 'http://another-example.com']
    METHODS = ['GET', 'POST', 'PUT', 'DELETE']
    ALLOW_HEADERS = ['*']
    SUPPORTS_CREDENTIALS = False
    MAX_AGE = 86400
    SEND_WILDCARD = True
    AUTOMATIC_OPTIONS = False
    VARY_HEADER = False


class AppConfig:
    API_KEY = 'your_secret_api_key'