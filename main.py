# coding=utf-8
from app.app import App
from dotenv import load_dotenv

if __name__ == '__main__':
    # Load .env variables
    load_dotenv()

    # Start app
    app = App()
    app.start()

    exit(0)
