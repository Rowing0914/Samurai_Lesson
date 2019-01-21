from flask import Flask, render_template
import logging, datetime, sys

api = Flask(__name__)

def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('log.txt', mode='w')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger

@api.route('/')
def index():
	logger.info('hello world')
	return render_template('index.html')

if __name__ == '__main__':
	logger = setup_custom_logger('myapp')
	api.run(host='0.0.0.0')