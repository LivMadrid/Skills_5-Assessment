"""Skills 5: SQLAlchemy & AJAX

This file is used in Part 2 and 3 of Skills 5: SQLAlchemy & AJAX. You need to
complete Part 1 first, otherwise this part of the assessment won't work.
"""

from model import db, Human, Animal


def get_human_2():
    """Return the human with the id 2."""

    # human_2 = (db.session.query(Human).filter(Human.human_id == 2).one())
    # return human_2
    return print(db.session.query(Human).filter(Human.human_id == 2).one())
    
def get_first_fish():
    """Return the FIRST animal with the species 'fish'."""

    return print(db.session.query(Animal).filter(Animal.animal_species == 'fish').first())

def get_young_animals():
    """Return all animals that were born after 2015.

    Do NOT include animals without birth years.
    """
    return db.session.query(Animal).filter(Animal.birth_year > '2015', Animal.birth_year != None).all()

def get_j_names():
    """Return the humans with first names that start with 'J'."""

    return print(db.session.query(Human).filter(Human.fname.like('J%')).all())

def get_null_bdays():
    """Return all animals whose birth years are NULL."""

    return db.session.query(Animal).filter(Animal.birth_year == None).all()

def get_fish_or_rabbits():
    """Return all animals whose species is 'fish' OR 'rabbit'."""

    return print(db.session.query(Animal).filter(db.or_(Animal.animal_species.like('%fish%'), Animal.animal_species.like('%rabbit%'))).all())

def print_directory():
    """Output a list of humans and their animals.

    For example:

    >>> print_directory()
    Justin Time
    - Peter (rabbit)
    - Peppa (pig)
    Carmen Sandiego
    - Blub (fish)

    You may only use ONE query to retrieve initial data. (Hint: leverage a
    SQLAlchemy relationship to retrieve additional information)
    """
    # humans_and_animals = db.session.query(Human.fname,
    #                 Human.lname,
    #                 Animal.name,
    #                 Animal.animal_species).join(Animal)
    
    # # all_humans_all_animals =  humans_and_animals.group_by(Human.fname, Human.lname, Human.human_id, Animal.name, Animal.animal_species)

    # all_humans_all_animals = humans_and_animals.all()

    # for fname, lname, name in all_humans_all_animals :
    #     return fname, lname, name   # this above code errors saying that too many variables to unpack... expect 3 got 3 ...

    #this code works but only for one person:bob.... print_directory()>>>('Bob', 'Personne', 'Fluffy', 'cat')
    human_animal_directory_list = []

    directory_humans_animals = db.session.query(Human.fname,
                                                Human.lname,
                                                Animal.name,
                                                Animal.animal_species).join(Animal).all()

    for fname, lname, name, animal_species in directory_humans_animals:
        human_animal_directory_list.extend([fname, lname, name, animal_species])
        return human_animal_directory_list

def find_humans_by_animal_species(species):
    """Return a list of all humans who have animals of the given species.

    Each human should only appear once in the returned list. For example:

    >>> find_humans_by_animal_species('snake')

    Again, you may only use ONE query to retrieve initial data. (Hint: use a
    relationship! Also, you can pursue uniqueness in a Pythonic way --- you
    don't have to do it with pure SQLAlchemy)
    """
    # find_humans = db.session.query(Human.human_id).join(Animal).group_by(fname, lname).having(Animal.animal_species.like('%%'))

    find_humans = db.session.query(Human.fname,
                                   Human.lname,
                                   Animal.animal_species).join(Animal).filter(Animal.animal_species.like(':species')).all()
    
    # filter(Animal.animal_species.like('%%'))
    all_humans_by_species = []
    for fname, lname in find_humans: 
    #     return humans.fname,  humans.lname
        all_humans_by_species.extend([fname, lname])
        return print(all_humans_by_species)
    

if __name__ == '__main__':
    from server import app
    from model import connect_to_db

    connect_to_db(app)
