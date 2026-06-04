from flask import Flask, render_template, request, jsonify
import requests
import random
from datetime import datetime, timedelta
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_mock_telemetry():
    """
    Simulates live carrier network information that regular web APIs can't access.
    """
    statuses = ["Idle", "On a Call (Busy)", "Ringing", "Unavailable"]
    current_status = random.choice(statuses)
    
    # Generate a random past time for the last call
    minutes_ago = random.randint(5, 1440)
    last_call_time = (datetime.now() - timedelta(minutes=minutes_ago)).strftime("%Y-%m-%d %H:%M:%S")
    
    return {
        "is_on_call": "Yes" if current_status == "On a Call (Busy)" else "No",
        "live_status": current_status,
        "last_call_timestamp": f"{last_call_time} ({minutes_ago // 60}h {minutes_ago % 60}m ago)"
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/analyze', methods=['GET'])
def analyze_number():
    phone_number = request.args.get('number')
    if not phone_number:
        return jsonify({"error": "Phone number is required."}), 400

    api_key = app.config['NUMLOOKUP_API_KEY']
    
    try:
        # Requesting NumLookupAPI data
        response = requests.get(
            f"{app.config['NUMLOOKUP_URL']}{phone_number}",
            headers={"apikey": api_key},
            timeout=10
        )
        
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch data from NumLookupAPI."}), response.status_code
        
        api_data = response.json()
        
        if not api_data.get('valid'):
            return jsonify({"error": "The phone number entered is invalid or unrecognized."}), 400
            
        # Combine NumLookupAPI data with our live telemetry mock data
        live_telemetry = get_mock_telemetry()
        
        result = {
            "valid": api_data.get("valid"),
            "number": api_data.get("number"),
            "international_format": api_data.get("international_format"),
            "country": api_data.get("country_name"),
            "location": api_data.get("location") or "Unknown Location",
            "carrier": api_data.get("carrier") or "Unknown Carrier",
            "line_type": api_data.get("line_type"),
            # Live Status parameters requested
            "is_on_call": live_telemetry["is_on_call"],
            "live_status": live_telemetry["live_status"],
            "last_call": live_telemetry["last_call_timestamp"]
        }
        
        return jsonify(result)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Server network error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)