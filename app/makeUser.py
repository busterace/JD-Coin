import base64


# print(base64.b85encode(b'ACEzxs75395145').decode())
import time
from pathlib import Path

# print(time.strftime('%Y%m%d',time.localtime()))

dayTime = time.strftime('%Y%m%d', time.localtime())
logFile = Path(__file__).parent.joinpath("../log/test" + dayTime + ".log")
logText = logFile.read_text()
print(logText)