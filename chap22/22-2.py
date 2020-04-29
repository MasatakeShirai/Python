#ログを出力する
import logging
import os

os.chdir('chap22')

logger = logging.getLogger('my_logger_name')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('log.out')

logger.addHandler(handler)

logger.debug('hello logger')

#ログファイルを標準出力する
import sys
stream_header = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_header)
logger.debug('Hello sysout')

#重要度の設定
# この場合はwarning以上のもののみが出力される
logger.setLevel(logging.WARNING)
logger.debug('Debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')

#書式の設定
formater = logging.Formatter(
    'Name=%(name)s Level=%(levelname)s Time=%(asctime)s Message=%(message)s'
    )
handler.setFormatter(formater)
logger.setLevel(logging.DEBUG)
logger.debug('hello formatter')

#共通設定
logging.basicConfig(
    filename='log.out',
    filemode='w',
    level=logging.DEBUG,
    format="%(levelname)s %(message)s",
)
logger = logging.getLogger('my_logger_name')

#ログのローテーション
# ログの量が一定量を超えた際に，前のログを上書きし容量を無制限に使うことを防ぐ
import logging.handlers
logger = logging.getLogger('my_logger_name')
logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler('log.out',maxBytes=10, backupCount=5)
logger.addHandler(handler)
for i in range(20):
    logger.debug(str(i))
    
