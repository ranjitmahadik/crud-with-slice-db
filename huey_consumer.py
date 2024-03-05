from huey.bin.huey_consumer import consumer_main
from config.config import load_config

if __name__ == "__main__":
    load_config()
    consumer_main()