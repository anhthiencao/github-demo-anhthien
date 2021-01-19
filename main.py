from app import app
from app.configs import config

if __name__ == "__main__":
    app.run(
        host=config['application']['host'],
        port=config['application']['port'],
        debug=config['application']['debug']
    )