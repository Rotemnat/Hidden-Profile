from os import environ

SESSION_CONFIGS = [
    dict(
        name='Hidden_Profile1',
        display_name='The Board Decision Game: Room 1 UB',
        app_sequence=['share_information1111', 'choice1111',
                      'share_information1221', 'choice1221',
                      'share_information1222', 'choice1222',
                      'share_information1121', 'choice1121',
                      'share_information1122', 'choice1122',
                      'payment_info'],
        num_demo_participants=4
    ),
    dict(
        name='Hidden_Profile2',
        display_name='The Board Decision Game: Room 2 BU',
        app_sequence=['share_information1111','choice1111',
                'share_information1121', 'choice1121',
                'share_information1122','choice1122',
                'share_information1221','choice1221',
                'share_information1222','choice1222',
                'payment_info'],
        num_demo_participants=4
    ),
    dict(
        name='Hidden_Profile_test',
        display_name='The Board Decision Game: Test Room1',
        app_sequence=['share_information1223', 'choice1223'],
        num_demo_participants=4
    ),
]
# 'share_information1111', 'choice1111' are the introduction apps

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.06, participation_fee=15.00, doc=""
)

PARTICIPANT_FIELDS = ['potential_payoff','selected_round','app_payoffs']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'he'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'NIS'
USE_POINTS = True

ROOMS = [
    dict(
        name='Room1',
        display_name='Room1',
        participant_label_file='_rooms/room1.txt',
    ),
    dict(
        name='Room2',
        display_name='Room2',
        participant_label_file='_rooms/room2.txt',
    ),

]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '5601403384302'

INSTALLED_APPS = ['otree']
