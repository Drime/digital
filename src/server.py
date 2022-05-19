from flask import *
from redis import Redis

app = Flask(__name__)
app.url_map.strict_slashes = False
redis = Redis(host= "redis", port=6379)

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    count = redis.incr("hits")
    score = redis.get("score")
    winner = redis.get("winner").decode("utf-8")
    won = int(count) == int(score)
    return render_template('index.html', winner=winner, won=won, count=count)

@app.route('/', methods=['POST'])
@app.route("/index", methods=["POST"])
def index_post():
    page_score = redis.get("score")
    score = int(request.form['score'])
    if int(page_score) == int(score):
        winner = request.form['text'].upper()
        redis.set("winner", winner)
        #return render_template('index.html', winner=winner, won=True, count=score)
        return index()
    else:
        return "cheater"

@app.route("/220519/reset/<int:count>", methods=["GET"])
def reset_count(count: int):
    redis.set("hits", count)
    redis.set("winner", "")
    return redis.get("hits")

@app.route("/220519/score/<int:new_score>", methods=["GET"])
def set_score(new_score: int):
    redis.set("score", new_score)
    redis.set("winner", "")
    return redis.get("score")

if __name__ == "__main__":
    redis.set("score", 228)
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )