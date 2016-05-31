import os
from flask import Flask
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from pythonapp import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

db.create_all()

if __name__ == '__main__':
    manager.run()




