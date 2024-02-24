import os
from os import getenv

API_ID = getenv("API_ID", "22114233")

API_HASH = getenv("API_HASH", "d7abcec5c967414fadb1d438fa05ebea")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6704979486:AAFwGWZZ4eLOErCuLQafTFypRdsIbF09S6c")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

sudo_group = -1002005463437
sudo_user = 1403488629
log_channel = -1002094254723

# try:
#     ADMINS=[]
#     for x in (os.environ.get("ADMINS", "5760012562 5044896938 6116624490 6230767081 5496342413 6347607291 6351476810").split()):
#         ADMINS.append(int(x))
# except ValueError:
#         raise Exception("Your Admins list does not contain valid integers.")
# ADMINS.append(OWNER)


