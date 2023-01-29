import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5819661777:AAENWaLREb9nAIHKaOKZ2SA7TPRHQXP0ipI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzsBu4XxyqctlEQ7IrTfO5V_PdBE0qAFxIAA4QWHdFmv8jyqOw5woBwjPiKfl2X8uX19VEOt9V9p0m2NgXVlrQHez3uCh2fnAptXPkTbs_2oOZDHPcdJVo1m-3g5iQ-N0OxNGVokdRjrUuYDhk0JqT1pwi2Tl9FLjhJ7w5wHglDJtbxWPtUTZFM989pADA9a3RrWRflhjfKwDHAVNa31OXWjHd64OmS0ob4lHkUt_W7CpPwBRze1EkesMkPC3afhMmOjkpniPLc8cYNoCXyW6265XVJKEzYXG2XyAUKQtp2-9u_H9BQNdnF4Rp4S0rLzvH-tDSgND-TRWAlgYEzzEsr7kMU=
")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Livs_robot")
    SUPPORT = os.environ.get("SUPPORT", "xd_area51") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "x_update") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://t.me/X_UPDATE/13")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5814665380")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
