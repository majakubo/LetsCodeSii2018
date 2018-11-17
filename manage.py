# manage.py

from flask_script import Manager, prompt_bool
from helpful_spirits import app, db
from helpful_spirits.models import *
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()
        print( 'Dropped the database')


if __name__ == "__main__":
    manager.run()
