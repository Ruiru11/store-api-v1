import os

from app import create_app

app = create_app(os.getenv('ENV') or 'dev')

if __name__ == "__main__":
    app.run()
 