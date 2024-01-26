from app.config import app

@app.route('/', methods=["GET"])
def index():
    return 'Hellow Worlds'