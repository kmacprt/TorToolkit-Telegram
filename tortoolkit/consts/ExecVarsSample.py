try:
    from .ExecVars import ExecVars
except:

    class ExecVars:
        PREFIX = "" # your prefix here
        # Set true if its VPS
        IS_VPS = False

        API_HASH = "d4fe9ba56710f216251c2818fc50ebef"
        API_ID = 1340081
        BOT_TOKEN = "1596550006:AAFfTpjyXPvUPci5IVzB3TkKd4en3iKuzaA"
        BASE_URL_OF_BOT = "https://t.me/torleechpro_bot"

        # Edit the server port if you want to keep it default though.
        SERVPORT = 80

        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [-1001432480057, -1001390893086]
        OWNER_ID = 1156597097

        # Google Drive Index Link should include the base dir also See readme for more info
        GD_INDEX_URL = "https://lkhitechmirror3.lkhitech8.workers.dev/2:/noswDY0Zl0g.mp4"

        # Time to wait before edit message
        EDIT_SLEEP_SECS = 10

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 1700000000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress
        COMPLETED_STR = "▰"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "▱"

        # DB URI for access
        DATABASE_URL = (
            "postgres://jxbnqulieoxqjw:bd3647c7de4afbd89dc55285435a5b054c0c8efe8204acba19a35297d7825329@ec2-54-83-137-206.compute-1.amazonaws.com:5432/df024a8sn2ni3b"
        )

        # UNCOMMENT THE BELOW LINE WHEN USING CONTAINER AND COMMENT THE UPPER LINE
        # DATABASE_URL = "dbname=tortk user=postgres password=your-pass host=db port=5432"

        # MEGA CONFIG
        MEGA_ENABLE = False
        MEGA_API = ""
        MEGA_UNAME = None
        MEGA_PASS = None

        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = "/"

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = True

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = False

        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = ""

        # Max size of a playlist that is allowed (Number of videos)
        MAX_YTPLAYLIST_SIZE = 20

        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 10

        # Set this to your bot username if you want to add the username of your bot at the end of the commands like
        # /leech@TorToolkitBot so the value will be @TorToolkitBot
        BOT_CMD_POSTFIX = ""

        # Time out for the status Delete.
        STATUS_DEL_TOUT = 20

        # Allow the user settings to be accessed in private
        USETTINGS_IN_PRIVATE = False

        # Torrent max time to collect metadata in seconds
        TOR_MAX_TOUT = 180

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50, 10, 2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        EXPRESS_UPLOAD = True
