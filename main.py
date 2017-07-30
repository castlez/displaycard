import urllib
import json
from flask import request


from flask import Flask
app = Flask(__name__)
version = "0.1"

def get_page():
    return "<html><body><a>version {}</a><br><br>".format(version) + \
              '<form action="." method="POST"><input type="text" name="text"><input type="submit" name="my-form" value="Send"></form>' + \
              "<br><br>"

@app.route("/app", methods=['GET'])
def main():
    return get_page()


@app.route('/app', methods=['POST'])
def my_form_post():
    # card_name = "memnarch"
    card_name = request.form['text']
    with urllib.request.urlopen("https://api.deckbrew.com/mtg/cards?name={}".format(card_name)) as response:
        j = json.loads(response.read())
        multiverse_id = "220532"
        img = "https://image.deckbrew.com/mtg/multiverseid/{}.jpg".format(multiverse_id)
        img_html = "<img src=\"" + img + "\"/>"
        return get_page() + "<br><br>" + \
               img_html + \
               "</body></html>"

if __name__ == '__main__':
  app.run()