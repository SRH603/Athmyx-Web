from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/products/ai')
def ai():
    return render_template('ai.html')

@app.route('/products/game')
def game():
    return render_template('game.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/apps')
def apps():
    return render_template('apps.html')

@app.route('/apps/a')
def app_a():
    return render_template('app_a.html')

@app.route('/apps/b')
def app_b():
    return render_template('app_b.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/support/contact')
def contact():
    return render_template('contact.html')

@app.route('/support/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
