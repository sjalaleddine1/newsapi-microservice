import json, requests
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5555")

while True:
    message = socket.recv_json()
    message = json.loads(message)
    country, news_outlet = message[0], message[1]
    print("Received request: %s" % message)

    url = "https://newsapi.org/v2/" \
              "top-headlines?country={}&apiKey=6db89d56e492480593a9e23072586219".format(country)
    req = requests.get(url)
    req = req.json()
    title = desc = link = ""
    articles = req["articles"]

    for article in articles:
        if article["source"]["name"] == news_outlet:
            title = article["title"]
            desc = article["description"]
            link = article["url"]
    res = [title, desc, link]
    json_res = json.dumps(res)

    socket.send_json(json_res)