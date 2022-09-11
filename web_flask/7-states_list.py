#!/usr/bin/python3
""" first flask file
    """
from flask import Flask
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """desplay html file """
    all_states = storage.all(State).values()
    return render_template('7-states_list.html', all_states=all_states)


@app.teardown_appcontext
def close_sqlalchemy(exception):
    """remove the  SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
