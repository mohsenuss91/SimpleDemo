#!/usr/bin/env python
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    return render_template('title.html', name=name)

@app.route('/frame/')
@app.route('/frame/<name>')
def frameRender(name=None):
  return render_template('frame.html', name=name)


if __name__ == '__main__':
    app.debug = True
    app.run()
