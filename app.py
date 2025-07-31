from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/logout')
def logout():  
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)