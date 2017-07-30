import urllib
import json


from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
   with urllib.request.urlopen('https://api.deckbrew.com/mtg/cards?name=memnarch') as response:
       j = json.loads(response.read())[0]
       # json_string = json.dumps(j, indent=4, sort_keys=True)
       img = "https://image.deckbrew.com/mtg/multiverseid/220532.jpg"
       img_html = "<img src=\"" + img + "\"/>"
       return "<html><body>" + img_html +"</body></html>"



if __name__ == '__main__':
  app.run()