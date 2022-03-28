# 常用调试logging

import logging

# 创建通用log对象
def getlog(level, logfile=None):
    # 创建logger
    logger = logging.getLogger()
    logger.setLevel(level)   # log等级总开关
    
    # 定义handler的输出格式
    formatter = logging.Formatter("[%(levelname)s] %(asctime)s : %(message)s")

    # 创建handler，用于写入日志文件
    if logfile:
        logfile = logfile
        file_handler = logging.FileHandler(logfile, mode='w')
        # 将logger添加到handler里面
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # 创建handler，用于输出到控制台
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    # stream_handler.setLevel(logging.INFO)   # 不同handler可以设置不同的log等级

    # 将logger添加到handler里面
    logger.addHandler(stream_handler)

    return logger

if __name__ == "__main__":
    print("This is a logging tool")
