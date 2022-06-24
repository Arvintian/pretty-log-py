# -*- coding:utf-8 -*-

from pretty_logging import pretty_logger
import time

start = time.time()
i = 0
while i < 100:
    pretty_logger.info("info---sss--{}".format(i))
    i += 1
print(time.time() - start)
