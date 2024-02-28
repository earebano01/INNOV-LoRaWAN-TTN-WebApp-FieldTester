import requests
import json
import datetime

# Définition des paramètres pour l'API TTN
cluster = "nam1"
application = "ncrc-1173-mkrwan-1310"
app_key = "NNSXS.T4KWNY3LYSGIGS6YI3ES57QIB3SZ63C43QKMMXY.RKU3O2I6J5SRIK535YXWS4R7TPDBYQK5X4OFWEGNBGCHTOKW3OWQ"

def get_new_data():
    # Durée depuis laquelle récupérer les données (en secondes)
    last_seconds = 3600  
    
    # Pour chaque périphérique spécifié
    for each_device in ["eui-a8610a34363a9216"]:  
        # Construction des URL pour obtenir les données de charge utile et de métadonnées
        payload_endpoint = f"https://{cluster}.cloud.thethings.network/api/v3/as/applications/{application}/devices/{each_device}/packages/storage/uplink_message?order=-received_at&field_mask=up.uplink_message.decoded_payload&time={last_seconds}s"
        metadata_endpoint = f"https://{cluster}.cloud.thethings.network/api/v3/as/applications/{application}/devices/{each_device}/packages/storage/uplink_message?order=-received_at&field_mask=up.uplink_message.rx_metadata&time={last_seconds}s"
        
        # Création de l'en-tête d'authentification
        key = f'Bearer {app_key}'
        headers = {'Authorization': key}

        try:
            # Requête pour obtenir les données de charge utile
            payload_response = requests.get(payload_endpoint, headers=headers)
            if payload_response.status_code != 200:
                print("La requête de charge utile a échoué :", payload_response.reason)
                continue
            
            # Requête pour obtenir les données de métadonnées
            metadata_response = requests.get(metadata_endpoint, headers=headers)
            if metadata_response.status_code != 200:
                print("La requête de métadonnées a échoué :", metadata_response.reason)
                continue

            # Traitement des données obtenues
            process_data(each_device, payload_response, metadata_response)

        except Exception as e:
            print("Erreur lors du traitement de la réponse :", e)

def process_data(each_device, payload_response, metadata_response):
    try:
        # Extraction des données JSON de la réponse
        payload_data = payload_response.json().get("data", [])
        metadata_data = metadata_response.json().get("data", [])
    except json.JSONDecodeError as e:
        print("Erreur lors du décodage de la réponse JSON :", e)
        print("Texte de la réponse de charge utile :", payload_response.text)
        print("Texte de la réponse de métadonnées :", metadata_response.text)
        return
    
    # Parcours des données de charge utile et des métadonnées
    for payload_item, metadata_item in zip(payload_data, metadata_data):
        # Extraction des informations pertinentes de la charge utile
        result = payload_item.get("result", {})
        uplink_message = result.get("uplink_message", {})
        decoded_payload = uplink_message.get("decoded_payload", {})
        received = result.get("received_at", "")
        lat = decoded_payload.get("latitude", "")
        lon = decoded_payload.get("longitude", "")
        temp = decoded_payload.get("temperature", "")
        humidity = decoded_payload.get("humidity", "")
        
        # Extraction des informations pertinentes des métadonnées
        rx_metadata = metadata_item.get("result", {}).get("uplink_message", {}).get("rx_metadata", [{}])[0]
        rssi = rx_metadata.get("rssi", "")
        snr = rx_metadata.get("snr", "")
        gateway_id = rx_metadata.get("gateway_ids", {}).get("gateway_id", "")
        
        # Affichage des données extraites
        print("Identifiant de la passerelle :", gateway_id)
        print("Identifiant du périphérique :", each_device)
        print("Latitude :", lat)
        print("Longitude :", lon)
        print("Température :", temp)
        print("Humidité :", humidity)
        print("RSSI :", rssi)
        print("SNR :", snr)
        print("-------------------------")

# Appel de la fonction pour récupérer les nouvelles données
get_new_data()
