from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.init_app(app)
    app.app_context().push()
    return db


DEFAULT_IMAGE_URL = "https://tinyurl.com/demo-cupcake"

"""Models for Cupcake app."""
class Cupcake(db.Model):
    
    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.Text, 
                       nullable=False)
    size = db.Column(db.Text,
                     nullable=False)                       
    rating = db.Column(db.Float, 
                   nullable=False )
    image = db.Column(db.Text, 
                      default=DEFAULT_IMAGE_URL)
    
    def serialize(self):
        return {
            "id" : self.id,
            "flavor" : self.flavor,
            "size" : self.size,
            "rating" : self.rating,
            "image": self.image
        }
    def __rep__(self):
        return (f"<Cupcake {self.id} - {self.flavor}>")                

    







