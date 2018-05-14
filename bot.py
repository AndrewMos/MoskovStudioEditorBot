import os
import logging
import importlib
from telegram.ext import Updater
from telegram.ext.dispatcher import run_async

updater = Updater(token=os.environ.get('542435999:AAGc2SbUeZuj2K5Ie1FJzf8W9UzORDc1-LY') or "")
dispatcher = updater.dispatcher

logging.basicConfig(format='[%(asctime)s][%(name)s][%(levelname)s] %(message)s',
	level=logging.INFO)

logger = logging.getLogger(__name__)

@run_async
def error_callback(bot, update, error):
	pass # p-t-b's logger already logs this to the console

def main():
	for modname in ["compressor", "help"]:
		module = getattr(importlib.import_module('modules.{}'.format(modname)), "module") # from modules.modname import module
		logger.info("importing module: %s (handlers: %d)", module.name, len(module.handlers))
		for handler in module.handlers:
			dispatcher.add_handler(handler)

	dispatcher.add_error_handler(error_callback)

	updater.start_polling(clean=True)
	updater.idle()

if __name__ == '__main__':
	main()
