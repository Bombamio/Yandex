import logging
from logging.handlers import RotatingFileHandler


# Глобальная конфигурация для всех леггеров.
logging.basicConfig(
    filename='myapp.log',
    encoding='utf-8',
    filemode='w',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s, %(lineno)d',
)


# Индвидуальные настройки логгера для этого файла.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(
    'my_logger.log',
    maxBytes=50000000,
    backupCount=5,
    encoding='utf-8',
)
handler.setFormatter(logging.Formatter(
    '%(asctime)s, %(levelname)s, %(message)s, %(name)s, %(lineno)d'
))
logger.addHandler(handler)


logger.debug('123')
logger.info('Сообщение отправлено')
logger.warning('Большая нагрузка!')
logger.error('Бот не смог отправить сообщение')
logger.critical('Всё упало! Зовите админа!1!111')
