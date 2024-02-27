#!/usr/bin/python3

import requests
import json

# Replace these values with your own
theApplication = "ncrc-1173-mkrwan-1310"
theAPIKey = "NNSXS.T4KWNY3LYSGIGS6YI3ES57QIB3SZ63C43QKMMXY.RKU3O2I6J5SRIK535YXWS4R7TPDBYQK5X4OFWEGNBGCHTOKW3OWQ"

# Note the path you have to specify. Double note that it has to be prefixed with 'up.'.
theFields = "up.uplink_message.decoded_payload,up.uplink_message.frm_payload,up.uplink_message.rx_metadata"

theNumberOfRecords = 20

theURL = f"https://nam1.cloud.thethings.network/api/v3/as/applications/{theApplication}/packages/storage/uplink_message?order=-received_at&limit={theNumberOfRecords}&field_mask={theFields}"

# These are the headers required in the documentation.
theHeaders = { 'Authorization': f'Bearer {theAPIKey}' }

print("\n\nFetching from data storage  ...\n")

try:
    r = requests.get(theURL, headers=theHeaders)
    print("URL:", r.url)
    print("Status:", r.status_code)
    print("Response:")
    print(r.text)

    # Parse the response into JSON format
    parsed_response = json.loads(r.text)
    print("Parsed JSON:")
    print(json.dumps(parsed_response, indent=4))

except Exception as e:
    print("An error occurred:", e)


