import json

from flask import Flask

app = Flask(__name__)

@app.route("/search/<room_id>")
def search_room(room_id):
    return json.dumps({'id': room_id})


if __name__ == "__main__":
    app.run(debug=True, port=8001)
