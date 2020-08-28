# Motivational Puppy Meme Generator


The goal of this project is to build a "meme generator"—a multimedia application to dynamically generate memes, including an image with an overlaid quote

![demo gif](./demo.gif)

The live version can be accessed [here](https://thawing-spire-21589.herokuapp.com)

# Running Locally

## Installation

To get started, please make sure you have Docker installed on your system. You can download it here [here](https://docs.docker.com/get-docker/)

## Setting

### Build Docker Image

Run the following in a terminal to build the Docker image

```bash
    $ docker image build --tag meme_generator .
```

## Start the App

```bash
    $ docker run -p 5000:5000 meme_generator
```

Now go to http://127.0.0.1:5000 to access the app
