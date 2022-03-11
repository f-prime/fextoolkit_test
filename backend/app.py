from flask import Flask, request, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)
cache = []

def populate_cache():
    with open("data/phonebook.csv") as phonebook: 
        phonebook_csv_reader = csv.reader(phonebook)
        for row in phonebook_csv_reader:
            first_name, last_name, state, phonenumber = row
            row_to_search_match_dict = {
                "first_name": first_name,
                "last_name": last_name,
                "state": state,
                "phonenumber": phonenumber
            }
            cache.append(row_to_search_match_dict)

def search_phone_book(**kwargs):
    search_first_name = kwargs.get("first_name")
    search_last_name = kwargs.get("last_name")
    search_state = kwargs.get("state")
    offset = int(kwargs.get("offset") or 0)
    limit = int(kwargs.get("limit") or 100)
    results = list(filter(lambda item: item["first_name"].lower() == search_first_name or item["last_name"].lower() == search_last_name or item["state"].lower() == search_state, cache))
    items = results[offset:offset + limit]
    return {"items": items, "total": len(results), "count": len(items)}

@app.route("/search/", methods=['GET'])
def search_phonebook():
    first_name = request.args.get("firstName").lower()
    last_name = request.args.get("lastName").lower()
    state = request.args.get("state").lower()
    limit = request.args.get("limit")
    offset = request.args.get("offset")

    if not any([first_name, last_name, state]):
        return jsonify({"error": "At least one of the three fields must be filled."}), 400

    search_results = search_phone_book(
        first_name=first_name, 
        last_name=last_name, 
        state=state,
        limit=limit,
        offset=offset
    )

    return jsonify(search_results)

if __name__ == "__main__":
    populate_cache()
    app.run(debug=True, port=8080, threaded=True)
