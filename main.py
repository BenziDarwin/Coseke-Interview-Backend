import json
from flask import Flask, request

app = Flask(__name__)


@app.route("/o-level", methods=["GET"])
def get_o_level_scripts():
    if request.method == "GET":
        file = open("o-level.json")
        data = json.load(file)
        file.close()
        return data


@app.route("/o-level/add-file", methods=["POST"])
def post_o_level_scripts():
    file = open("o-level.json", "+w")
    data = json.load(file)
    new_data = data.append(request.get_json())
    json.dump(new_data, file)
    file.close()
    print("Successfully added data!")
    return "", 204


@app.route("/o-level/delete", methods=["POST"])
def delete_o_level_scripts():
    file = open("o-level.json", "+w")
    data: list = json.load(file)
    new_data = list(
        filter(
            lambda val: val["random_code"] != request.get_json()["random_code"], data
        )
    )
    json.dump(new_data, file)
    file.close()
    print("Successfully deleted data!")
    return "", 204


@app.route("/a-level", methods=["GET"])
def get_a_level_scripts():
    if request.method == "GET":
        file = open("a-level.json")
        data = json.load(file)
        file.close()
        return data


@app.route("/a-level/add-file", methods=["POST"])
def post_a_level_scripts():
    file = open("a-level.json", "a")
    data: list = json.load(file)
    new_data = data.append(request.get_json())
    json.dump(new_data, file)
    file.close()
    print("Successfully added data!")
    return "", 204


if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
