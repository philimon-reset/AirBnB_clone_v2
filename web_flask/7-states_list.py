#!/usr/bin/python3
"""Flask framework
"""
from flask import Flask, url_for, render_template, request
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db():
    if storage is not None:
        storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ list of state ids
    """
    data = storage.all(State)
    teardown_db()
    return render_template('7-states_list.html', total=data.values())


if __name__ == '__main__':
    app.run()
