from flask import Flask,request
from threading import Thread
from visit_embed import visit
from result_embed import result

app = Flask('')

@app.route('/')
def home():
    return "I'm alive no cap"

@app.route('/send-visit', methods=['GET','POST'])
def visit_embed():
    return visit()

@app.route('/send-result', methods=['GET','POST'])
def result_embed():
    return result()

def keep_alive():
    t = Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 8080})
    t.start()

if __name__ == "__main__":
    keep_alive()
