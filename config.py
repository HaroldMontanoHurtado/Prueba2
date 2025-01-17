class CORSConfig:
    ORIGINS = ['http://example.com', 'http://another-example.com']
    METHODS = ['GET', 'POST', 'PUT', 'DELETE']
    ALLOW_HEADERS = ['Authorization', 'Content-Type']
    SUPPORTS_CREDENTIALS = False
    MAX_AGE = 3600
    SEND_WILDCARD = False
    AUTOMATIC_OPTIONS = False
    VARY_HEADER = True

# Configuración general de la aplicación
class AppConfig:
    API_KEY = "your_secret_api_key"
