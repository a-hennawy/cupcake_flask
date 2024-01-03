"""Blogly application."""

from flask import Flask, jsonify, request, render_template
from models import connect_db, Cupcake
from forms import new_cupcake_form

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mac@localhost:5432/cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'

db = connect_db(app)
db.create_all()

@app.route("/")
def index_page():
    form = new_cupcake_form()
    return render_template('index.html', form = form)

@app.route("/api/cupcakes")
def list_cup_cakes():
    cupcakes = Cupcake.query.all()
    serialized_list = [cake.serialize() for cake in cupcakes]
    return jsonify(cupcakes = serialized_list)


@app.route("/api/cupcakes/search")
def flavor_search():
    flavor = request.args["search"]
    # flavor = 'ch'
    searched_cupcakes = Cupcake.query.where(Cupcake.flavor.like(f"%{flavor}%")).all()
    serialized_cupcakes = [cupcake.serialize() for cupcake in searched_cupcakes]
    return jsonify(cupcakes = serialized_cupcakes)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes", methods=["POST"])
def post_cupcake():
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating= request.json["rating"]
    image = request.json.get("image")
    
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()
    res_json = new_cupcake.serialize()
    return (jsonify(cupcake=res_json), 201)

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating= request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message=("Cupcake deleted"))
