import random
import os
import requests
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor
import glob
import uuid
import shutil
from random import choice
import os
from meme import generate_meme
from pathlib import Path

app = Flask(__name__)

meme = MemeEngine("./static")


def setup():
    """ Load all resources """

    quote_files = ["./_data/DogQuotes/DogQuotesTXT.txt",
                   "./_data/DogQuotes/DogQuotesDOCX.docx",
                   "./_data/DogQuotes/DogQuotesPDF.pdf",
                   "./_data/DogQuotes/DogQuotesCSV.csv"]

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = glob.glob(images_path+"*.jpg") + glob.glob(images_path+"*.png")

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array
    quotes, images = setup()
    img = choice(images)
    quote = choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """ User input for meme information """
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    image_extension = None
    image_url = request.form.get("image_url", None)
    body = request.form.get("body", None)
    author = request.form.get("author", None)
    path = None
    download_path_name = None
    try:
        req = requests.get(url=image_url)
        if req.status_code == 200:
            content_type = req.headers.get("Content-Type")
            if content_type in ["image/png", "image/jpeg", "image/jpg"]:
                image_extension = content_type.split('/')[-1]
                file_name = str(uuid.uuid4())
                download_path_name = os.path.join("static/", f"{file_name}.{image_extension}")
                img_name = f"{file_name}.{image_extension}"
                with open(download_path_name, "wb") as f:
                    f.write(req.content)
                    f.close()

    except Exception as e:
        print("Error uploading", e)

    if download_path_name is not None:
        path = Path(generate_meme(download_path_name, body=body, author=author))
        os.remove(download_path_name)


    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
