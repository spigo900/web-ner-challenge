"""Flask backend which serves the model's NER tags for an input text.
"""
import os
from pathlib import Path
import pickle
from typing import Mapping, Protocol

from flask import Flask, request
from flask_cors import CORS


repo_root = Path(__file__).resolve().parent.parent
default_model_path = repo_root / "models" / "ner_tagger.pickle"

app = Flask(__name__)
ors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["MODEL_PATH"] = Path(os.getenv("MODEL_PATH", default_model_path))

NER_TAG_KEY = "ner"


@app.route("/ner", methods=["POST"])
def named_entity_recognition():
    """Perform named entity recognition on an input text passed as form data.

    The text should be given passed using the form data "text" key.
    """
    ner_tags = ner_tagger.get_entities(request.form["text"])
    return {
        NER_TAG_KEY: [{"name": name, "type": type_} for name, type_ in ner_tags.items()]
    }


class NERTagger(Protocol):
    """A NER tagger which can extract named entities from an input text.
    """

    def get_entities(self, text: str) -> Mapping[str, str]:
        """Get a mapping from entities mentioned in the text to their entity type.

         The entity type must be one of PERSON, GPE, LOCATION, or ORG. One would like to use an enum for this but that
         would be annoying because the flask backend directory name contains a dash.
         """


class DumbNERTagger(NERTagger):
    """A placeholder NER tagger that does no real NER tagging.

    Intended for testing purposes only.
    """

    def get_entities(self, text: str) -> Mapping[str, str]:
        return {
            "Patrick": "PERSON",
            "Bikini Bottom": "LOCATION",
        }


try:
    with app.config["MODEL_PATH"].open("rb") as f:
        ner_tagger: NERTagger = pickle.load(f)
except FileNotFoundError:
    print(f"Couldn't load NER tagger {app.config['MODEL_PATH']}; falling back on placeholder.")
    ner_tagger = DumbNERTagger()
