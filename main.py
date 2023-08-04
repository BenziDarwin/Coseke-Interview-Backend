import json
from flask import Flask, request, jsonify
from marshmallow import ValidationError
from schemas import *

app = Flask(__name__)


# O-level routes
# API endpoints to the o-level files


# Route to get all scripts
@app.route("/o-level", methods=["GET"])
def get_o_level_scripts():
    if request.method == "GET":
        with open("o-level.json", "r") as file:
            data = json.load(file)
        return jsonify(data)


# Route to add a file
@app.route("/o-level/add-file", methods=["POST"])
def post_o_level_scripts():
    try:
        new_data = request.get_json()
        result = olevelSchema().load(new_data)
        with open("o-level.json", "r+") as file:
            data = json.load(file)

            data.append(result)
            file.seek(0)
            json.dump(data, file)
            file.truncate()
            print("Successfully added data!")
            return "", 204
    except ValidationError as err:
        return f"Error occurred while adding data.{err}", 403

    except Exception as e:
        return f"Error occurred while adding data: {e}", 500


# Route to update a file
@app.route("/o-level/update", methods=["PUT"])
def update_o_level_scripts():
    try:
        new_data = request.get_json()
        update_data = olevelSchema().load(new_data)
        with open("o-level.json", "r+") as file:
            data = json.load(file)
            if "random_code" not in update_data:
                return "Invalid body!", 403
            updated = False
            for val in data:
                if val["random_code"] == update_data["random_code"]:
                    val.update(update_data)
                    updated = True
            if updated == False:
                return "File not found", 404
            file.seek(0)
            json.dump(data, file)
            file.truncate()
            print("Successfully updated data!")
            return "", 204
    except ValidationError as err:
        return f"Error occurred while adding data.{err}", 403
    except Exception as e:
        print(f"Error: {e}")
        return "Error occurred while updating data.", 500


# Route to delete a file
@app.route("/o-level/delete", methods=["DELETE"])
def delete_o_level_scripts():
    try:
        with open("o-level.json", "r+") as file:
            data = json.load(file)
            request_data = request.get_json()
            if "random_code" not in request_data:
                return "Invalid body!", 403
            new_data = list(
                filter(
                    lambda val: val["random_code"] != request_data["random_code"], data
                )
            )
            if len(new_data) == len(data):
                return "File not found", 404
            file.seek(0)
            json.dump(new_data, file)
            file.truncate()  # Truncate the file to remove any extra content
            print("Successfully deleted data!")
            return "", 204
    except Exception as e:
        print(f"Error: {e}")
        return "Error occurred while deleting data.", 500


# A-level routes
# API endpoints to the a-level files
@app.route("/a-level", methods=["GET"])
def get_a_level_scripts():
    with open("a-level.json", "r") as file:
        data = json.load(file)
        return jsonify(data)


@app.route("/a-level/add-file", methods=["POST"])
def post_a_level_scripts():
    try:
        new_data = request.get_json()
        result = olevelSchema().load(new_data)
        with open("a-level.json", "r+") as file:
            data = json.load(file)

            data.append(result)
            file.seek(0)
            json.dump(data, file)
            file.truncate()
            print("Successfully added data!")
            return "", 204
    except ValidationError as err:
        return f"Error occurred while adding data.{err}", 403

    except Exception as e:
        return f"Error occurred while adding data: {e}", 500


@app.route("/a-level/delete", methods=["DELETE"])
def delete_a_level_scripts():
    try:
        with open("a-level.json", "r+") as file:
            data = json.load(file)
            request_data = request.get_json()
            if "random_code" not in request_data:
                return "Invalid body!", 403
            new_data = list(
                filter(
                    lambda val: val["random_code"] != request_data["random_code"], data
                )
            )
            if len(new_data) == len(data):
                return "File not found", 404
            file.seek(0)
            json.dump(new_data, file)
            file.truncate()  # Truncate the file to remove any extra content
            print("Successfully deleted data!")
            return "", 204
    except Exception as e:
        print(f"Error: {e}")
        return "Error occurred while deleting data.", 500


# Route to update a file
@app.route("/a-level/update", methods=["PUT"])
def update_a_level_scripts():
    try:
        new_data = request.get_json()
        update_data = olevelSchema().load(new_data)
        with open("a-level.json", "r+") as file:
            data = json.load(file)
            if "random_code" not in update_data:
                return "Invalid body!", 403
            updated = False
            for val in data:
                if val["random_code"] == update_data["random_code"]:
                    val.update(update_data)
                    updated = True
            if updated == False:
                return "File not found", 404
            file.seek(0)
            json.dump(data, file)
            file.truncate()
            print("Successfully updated data!")
            return "", 204
    except ValidationError as err:
        return f"Error occurred while adding data.{err}", 403
    except Exception as e:
        print(f"Error: {e}")
        return "Error occurred while updating data.", 500


if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
