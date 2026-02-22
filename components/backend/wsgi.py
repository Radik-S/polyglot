from polyglot.composites.web_server import app
from polyglot.composites.web_server import Settings

if __name__ == "__main__":
    app.run(
        host=Settings.http_settings.HOST,
        port=Settings.http_settings.PORT,
        debug=Settings.http_settings.IS_DEV_MODE,
    )
