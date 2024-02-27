path_db = '/var/ttn_tracker/ttn_tracker_database.db'

refresh_period_seconds = 15

start_lat = 47.6211 
start_lon = -65.67496

cluster = "nam1"

application = "ncrc-1173-mkrwan-1310"
app_key = "NNSXS.T4KWNY3LYSGIGS6YI3ES57QIB3SZ63C43QKMMXY.RKU3O2I6J5SRIK535YXWS4R7TPDBYQK5X4OFWEGNBGCHTOKW3OWQ"

devices = [
    "eui-a8610a34363a9216"
]

gateway_locations = [
    ('Gateway 01', 47.6211945, -65.67475),
    ('Gateway 02', 47.6516938, -65.67487)
]

bing_api_key = 'AvYvx0oLrNB_CUoKLJibjitGAD7bB4o8i1bJMsPJodKBW2FftQUNSjB-Kfp9aQ8y'


def config_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{db}'.format(db=path_db)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
