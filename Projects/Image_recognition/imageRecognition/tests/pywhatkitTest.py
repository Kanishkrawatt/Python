import pywhatkit
from datetime import datetime

pywhatkit.sendwhatmsg("+919013366855", "Hello", datetime.now().hour, datetime.now().minute +1)