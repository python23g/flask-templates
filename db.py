from tinydb import TinyDB

db = TinyDB('db.json', indent=4)


def featured_posts():
    featured = db.table('featured')
    return featured.all()

def recent_posts():
    recent = db.table('recent')
    return recent.all()

