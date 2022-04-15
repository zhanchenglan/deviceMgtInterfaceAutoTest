import logging
import configparser
import os
import sys
from logging.handlers import TimedRotatingFileHandler

level = logging.DEBUG

log = logging.getLogger(__name__)
log.setLevel(level)

# projectPath = baseUtil.getProjectPath()
# logPath = os.sep.join([projectPath, "src", "logs", "test.log"])
# print("logPath----------------:" + logPath)
# cf = configparser.ConfigParser()
# cf.read("D:\work\pythonCode\pythonprojectdemo\src\main\common\config.ini")
# logPath = cf.get("path", "logPath")
# print("logPath:"+logPath)
# handler = TimedRotatingFileHandler(logPath)
# handler.suffix = "%Y%m%d"
# handler.setLevel(level)

# print("sys.path=="+sys.path[0])
# filename = sys.path[0].split("tests")[0] + "/logs/test.log"
#filename = os.path.abspath(os.path.dirname(__file__))[:-15] + "/src/logs/test.log"
# filename = os.sep.join([os.path.abspath(os.path.dirname(__file__))[:-15], "src", "logs", "test.log"])
filename = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")) + "/logs/test.log"
handler = TimedRotatingFileHandler(filename)
handler.suffix = "%Y%m%d"
handler.setLevel(level)


console = logging.StreamHandler()
console.setLevel(level)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)

log.addHandler(handler)
log.addHandler(console)







