import json
import os

import openai
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    # if there is a data.json file, load it
    # if not, create a new one
    with open("data.json") as f:
        data = json.load(f)
except FileNotFoundError:
    with open("data.json", "w") as f:
        data = {"blog_posts": {}, "other": {"counter": 1}}
        json.dump(data, f)


def get_post_from_gpt3(title, description):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f'Write an article (minimum 150 words) for my blog, where title is: "{title}" and description looks like this: "{description}". Format it with HTML for my website. Do not outline the title or the description at the start of the article. Use the same language that is used in the title & description.\n\nRESULT:',
        temperature=0.7,
        max_tokens=1300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    content = response.choices[0].text
    return {"title": title, "description": description, "content": content.replace("\n\n", "<br>")}


@app.route("/blog-posts", methods=["GET"])
def get_blog_posts():
    # i + 1 since our counter starts at 1 
    # new_data = [{"id": i + 1, **data["blog_posts"][str(i + 1)]} for i in range(len(data["blog_posts"]))]
    new_data = [{"id": key, **value} for key, value in data["blog_posts"].items()]
    return jsonify(new_data), 200


@app.route("/blog-posts", methods=["POST"])
def create_blog_post():
    try:
        post = get_post_from_gpt3(
            title=request.json["title"], description=request.json["description"]
        )
    except KeyError:
        return jsonify({"error": "either title or description were not provided"}), 400
    data["blog_posts"][str(data["other"]["counter"])] = post
    data["other"]["counter"] += 1
    return jsonify({"id": data["other"]["counter"] - 1, **data["blog_posts"][str(data["other"]["counter"] - 1)]}), 201


@app.route("/blog-posts/<int:id>", methods=["GET", "DELETE"])
def get_blog_post(id):
    if request.method == "GET":
        try:
            return jsonify({"id": str(id), **data["blog_posts"][str(id)]}), 200
        except KeyError:
            return jsonify({}), 404
    elif request.method == "DELETE":
        try:
            del data["blog_posts"][str(id)]
            return jsonify({}), 204
        except KeyError:
            return jsonify({}), 404


if __name__ == "__main__":
    app.run()
    with open("data.json", "w") as f:
        json.dump(data, f)
