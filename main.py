import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/o-level", methods=["GET"])
def get_o_level_scripts():
    if request.method == "GET":
        with open("o-level.json", "r") as file:
            data = json.load(file)
        return jsonify(data)


@app.route("/o-level/add-file", methods=["POST"])
def post_o_level_scripts():
    try:
        with open("o-level.json", "r+") as file:
            data = json.load(file)
            new_data = request.get_json()
            data.append(new_data)
            file.seek(0)
            json.dump(data, file)
            file.truncate()
            print("Successfully added data!")
            return "", 204
    except Exception as e:
        print(f"Error: {e}")
        return "Error occurred while adding data.", 500


@app.route("/o-level/delete", methods=["DELETE"])
def delete_o_level_scripts():
    try:
        with open("o-level.json", "r+") as file:
            data = json.load(file)
            request_data = request.get_json()
            new_data = list(
                filter(
                    lambda val: val["random_code"] != request_data["random_code"], data
                )
            )
            if len(new_data) == len(data):
                print(f"Error: file not found!")
                return "Error occurred while deleting data.", 404
            file.seek(0)  # Move the file pointer to the beginning
            json.dump(new_data, file)
            file.truncate()  # Truncate the file to remove any extra content
            print("Successfully deleted data!")
            return "", 204
    except Exception as e:
        print(f"Error: {e}")
        return "Error occurred while deleting data.", 500


@app.route("/a-level", methods=["GET"])
def get_a_level_scripts():
    with open("o-level.json", "r") as file:
        data = json.load(file)
        return jsonify(data)


@app.route("/a-level/add-file", methods=["POST"])
def post_a_level_scripts():
    try:
        with open("a-level.json", "r+") as file:
            data = json.load(file)
            new_data = request.get_json()
            data.append(new_data)
            file.seek(0)  # Move the file pointer to the beginning
            json.dump(data, file)
            file.truncate()  # Truncate the file to remove any extra content
            print("Successfully added data!")
            return "", 204
    except Exception as e:
        print(f"Error: {e}")
        return "Error occurred while adding data.", 500


@app.route("/a-level/delete", methods=["DELETE"])
def delete_a_level_scripts():
    try:
        with open("a-level.json", "r+") as file:
            data = json.load(file)
            request_data = request.get_json()
            new_data = list(
                filter(
                    lambda val: val["random_code"] != request_data["random_code"], data
                )
            )
            if len(new_data) == len(data):
                print(f"Error: file not found!")
                return "Error occurred while deleting data.", 404
            file.seek(0)  # Move the file pointer to the beginning
            json.dump(new_data, file)
            file.truncate()  # Truncate the file to remove any extra content
            print("Successfully deleted data!")
            return "", 204
    except Exception as e:
        print(f"Error: {e}")
        return "Error occurred while deleting data.", 500


if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
