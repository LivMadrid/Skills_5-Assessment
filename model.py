"""Skills 5: SQLAlchemy & AJAX

Part 1: Define Model Classes
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Human(db.Model):
    """Data model for a human."""
    #define column attributes for table Humans 
    __tablename__ = 'humans'

    human_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

    #unique so user can't enter same email twice and have two human_id numbers
    #decided to put human_id and email for repr because both are unique and easily identifiable 
    def __repr__(self):
        """Show Human Info"""
        return f'<Human human_id={self.human_id} email={self.email}>'

class Animal(db.Model):
    """Data model for an animal."""
#define column attributes for table Animals 
    __tablename__ = 'animals'

    animal_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    human_id = db.Column(db.Integer, db.ForeignKey('humans.human_id'))
    name = db.Column(db.String, nullable=False)
    animal_species = db.Column(db.String, nullable=False)
    birth_year = db.Column(db.Integer)
    #birth_year is nullable 
    #Because animals could have same name I decided to include species as well to differentiate 

    human = db.relationship('Human', backref='animals')

    def __repr__(self):
        """Show Animal Info"""
        return f'<Animal animal_id={self.animal_id} name={self.name} animal_species={self.animal_species}>'


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///animals'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    print('Connected to db!')
