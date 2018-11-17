# manage.py

from flask_script import Manager 
from helpful_spirits import app, db
from helpful_spirits.models import *
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
