import os

from app import create_app

environment = os.getenv('ENV')
print('environment', environment)
app = create_app(environment)

if __name__ == "__main__":
    app.run()
