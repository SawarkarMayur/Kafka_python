from flask import Flask,render_template,Response
from pykafka import KafkaClient

app = Flask(__name__)

@app.route('/')
def index():
    return (render_template('index.html'))

#Consumer API
@app.route('/topic/<topicname>')
def get_messages(topicname):
    client = get_kafka_client()
    def events():
        for i in client.topics[topicname].get_simple_consumer():
            yield 'data:{0}\n\n'.format(i.value.decode())
    return Response(events(),mimetype="text/event-stream")

def get_kafka_client():
    return KafkaClient(hosts="localhost:9092")



if __name__ == "__main__":
    app.run(debug=True, port=5001)