"""fasttext-server"""

from flask import Flask, jsonify, request
from pyfasttext import FastText

app = Flask(__name__)
app.config.from_object("config")


model = FastText(app.config["MODEL_PATH"])


@app.route("/")
def info():
    """Return some information about the deployed model."""
    return jsonify({"nwords": model.nwords,
                    "nlabels": model.nlabels,
                    "labels": model.labels
                    })

@app.route("/representations", methods=['POST'])
def representations():
    """Return word representations from the model."""
    word = request.get_json()["word"]
    repr = model[word].tolist()
    print(repr)

    response = {"word": word,
                "repr": repr}

    return jsonify(response)


@app.route("/similarities", methods=['POST'])
def similar():
    """Return a word similiar to the word provided from the model."""
    words = request.get_json()["words"]
    similarity = model.similarity(words[0], words[1])

    response = {"words": words,
                "similarity": similarity}

    return jsonify(response)


@app.route("/neighbors", methods=['POST'])
def neighbors():
    """Return the word/s closest to the word provided from the model."""
    word = request.get_json()["word"]
    neighbor = model.nearest_neighbors(word, k=1)

    response = {"word": word,
                "neighbor": neighbor}

    return jsonify(response)

@app.route("/predictions", methods=['POST'])
def predictions():
    """Return label predictions for a sentence from the supervised model"""
    text = request.get_json()["text"]

    prediction = model.predict_single(text, k=1)

    response =  {"text": text,
                "prediction": prediction}

    return jsonify(response)



if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"],
            host=app.config["HOST"],
            port=app.config["PORT"])

