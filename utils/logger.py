import logging
import os
from datetime import datetime

class Logger:
    """自定义日志类，支持控制台输出和文件保存"""
    def __init__(self, name="EcommerceTest"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # 避免重复添加Handler
        if not self.logger.handlers:
            # 1. 控制台输出
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            
            # 2. 文件输出 (按日期命名)
            if not os.path.exists("logs"):
                os.makedirs("logs")
            log_file = f"logs/{datetime.now().strftime('%Y-%m-%d')}.log"
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setLevel(logging.DEBUG)

            # 设置日志格式
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            console_handler.setFormatter(formatter)
            file_handler.setFormatter(formatter)

            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

# 实例化一个全局的logger，方便其他文件直接导入使用
logger = Logger().get_logger()