import os


# -------------------------------------------------------------------------------------------------
# PATHS
# -------------------------------------------------------------------------------------------------
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_PATH = "images/"
TO_OPEN_FILE_NAME = 'pyth.jpg'

# -------------------------------------------------------------------------------------------------
# GUI
# -------------------------------------------------------------------------------------------------
MAIN_WIN_TITLE = 'Image Evolution'
CHOOSE_DIALOG_MSG = "Choose an Evolution Image"

# -------------------------------------------------------------------------------------------------
# OPT SCHEME
# -------------------------------------------------------------------------------------------------
# defines the maximum error of color difference in percent
MAX_ALLOWED_ERROR_PERCENT = 5 # less value -> more precise output & longer time to generate
MAX_CIRCLE_RADIUS_PERCENT = 3 # less value -> smaller circle radius -> more precise output -> longer time to fill

# -------------------------------------------------------------------------------------------------
# LOG
# -------------------------------------------------------------------------------------------------
LOG_FORMAT = '%(levelname)s' + '\t' + '[%(asctime)s]' + '\t' +  '[%(filename)s:%(lineno)s]' + '\t' + '%(message)s'
DBG_ON = False



