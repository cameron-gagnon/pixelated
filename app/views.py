from flask import render_template, flash, redirect, request, session, url_for
from app import app
import time


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Pixelate')

@app.route('/signal/<opcode>')
def signal(opcode):
    print 'Sending signal: %d ' % (opcode)

#    retCode = subprocess.call(['sudo', './pixelated', opcode])

#    if not retCode:
#        print 'ERROR: exited with status: %d ' % retCode
    return redirect( url_for('index') )
