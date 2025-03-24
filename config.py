import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

BACKGROUND_IMAGE = os.path.join(BASE_DIR, 'templates', 'background-image.png')
BACKGROUND_BUTTON_IMAGE = os.path.join(BASE_DIR, 'templates', 'background-button.png')
BACKGROUND_BUTTON_HOLD_IMAGE = os.path.join(BASE_DIR, 'templates', 'background-button-hold.png')

WHITE = '#FFFFFF'
BLACK = '#000000'
ENTRY_COLOR = '#C0DBEA'

DB_PATH = os.path.join(BASE_DIR, 'database', 'users.db')