from flask import *
from redis import Redis

app = Flask(__name__)
redis = Redis(host= "redis", port=6379)

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET", "POST"])
def index():
    count = redis.incr("hits")
    won = count == 100
    return render_template('index.html',unique=unique ,won=won, count=count)

@app.route("/1061334/<int:count>", methods=["GET"])
def reset(count: int):
    redis.set("hits", count)
    return "ok"

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )