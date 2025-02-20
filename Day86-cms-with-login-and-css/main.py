from datetime import datetime
import os, sqlite3

from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = os.environ['SESSION_SECRET']  # Set this in Replit secrets

# Get credentials from Replit secrets
ADMIN_USERNAME = os.environ['ADMIN_USERNAME']
ADMIN_PASSWORD = os.environ['ADMIN_PASSWORD']
DB_NAME = 'entries.db'


class Entry:

    def __init__(self, date, title, body):
        self.date = date
        self.title = title
        self.body = body

    @classmethod
    def from_db_row(cls, row):
        """Create an Entry from a database row"""
        date = datetime.strptime(row[0], '%Y-%m-%d').date()
        return cls(date, row[1], row[2])


def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            date DATE NOT NULL,
            title TEXT NOT NULL,
            body TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def get_entries():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT date, title, body FROM entries ORDER BY date DESC')
    entries = [Entry.from_db_row(row) for row in c.fetchall()]
    conn.close()
    return entries


@app.route('/', methods=['GET'])
def index():
    entries = get_entries()
    return render_template('cms.tpl.html', entries=entries)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        session['logged_in'] = True
        flash('Successfully logged in!', 'success')
    else:
        flash('Invalid credentials!', 'error')

    return redirect(url_for('index'))


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/create', methods=['POST'])
def create_entry():
    if not session.get('logged_in'):
        flash('Please log in first!', 'error')
        return redirect(url_for('index'))

    try:
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        entry = Entry(date, request.form['title'], request.form['body'])

        # Then save to database
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO entries (date, title, body) VALUES (?, ?, ?)',
                  (entry.date.strftime('%Y-%m-%d'), entry.title, entry.body))
        conn.commit()
        conn.close()

        flash('Entry created successfully!', 'success')
    except Exception as e:
        flash(f'Error creating entry: {str(e)}', 'error')

    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=8080)
