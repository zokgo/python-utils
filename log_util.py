# -*- coding: utf-8 -*-
import os
import logging


from logging import handlers


LOG_PATH = "./log"
LOG_FILE_NAME = "service_name"
LOG_LEVEL = "info" # can use info debug warning error and critical


class Logger(object):
    # 日志级别关系映射
    level_relations = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }

    def __init__(
            self,
            filename=f"{LOG_PATH}/{LOG_FILE_NAME}.log",
            level=LOG_LEVEL,
            encoding="utf-8",
            when="midnight",
            backCount=7,
            fmt="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"):
        # 检测文件存放目录，不存在则创建
        os.makedirs(f"{LOG_PATH}", exist_ok=True)
        self.logger = logging.getLogger(filename)
        # 防止屏幕多次输出日志内容
        self.logger.handlers.clear()
        # 设置日志格式
        format_str = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")
        # 设置日志级别
        self.logger.setLevel(self.level_relations.get(level))

        # 屏幕打印日志
        sh = logging.StreamHandler()
        # 设置屏幕显示格式
        sh.setFormatter(format_str)
        # 向文件里写入日志 & 指定间隔时间自动生成文件的处理器
        th = handlers.TimedRotatingFileHandler(
            filename=filename,
            when=when,
            backupCount=backCount,
            encoding=encoding)
        # 设置文件写入格式
        th.setFormatter(format_str)
        self.logger.addHandler(sh)
        self.logger.addHandler(th)



if __name__ == '__main__':
    # 日志调用方法如下：
    # from utils.log import Logger
    # logger = Logger().logger
    logger = Logger().logger
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
