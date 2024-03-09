path_db = '/var/ttn_tracker/ttn_tracker_database.db' # Chemin de la base de données SQLite

refresh_period_seconds = 15 # Période de rafraîchissement en secondes

start_lat = 47.6211 # Latitude de départ
start_lon = -65.67496 # Longitude de départ

cluster = "nam1" # Cluster utilisé

application = "ncrc-1173-mkrwan-1310" # Application utilisée
app_key = "NNSXS.T4KWNY3LYSGIGS6YI3ES57QIB3SZ63C43QKMMXY.RKU3O2I6J5SRIK535YXWS4R7TPDBYQK5X4OFWEGNBGCHTOKW3OWQ" # Clé d'application

devices = [ # Liste des appareils
    "eui-a8610a34363a9216"
]

gateway_locations = [ # Emplacements des passerelles
    ('ccnb-ido-gw', 47.6211945, -65.67475),
    ('KonaGWInnov', 47.6516938, -65.67487)
]

bing_api_key = 'AvYvx0oLrNB_CUoKLJibjitGAD7bB4o8i1bJMsPJodKBW2FftQUNSjB-Kfp9aQ8y' # Clé API Bing Maps


def config_app(app):
    # Configuration de l'application Flask pour utiliser la base de données SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{db}'.format(db=path_db)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
