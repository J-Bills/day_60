from flask import Flask, render_template, request
from post import Post

app = Flask(__name__)

@app.route('/')
def index():
    posts_data = Post()
    posts_list = posts_data.get_blog_collection()
    return render_template("index.html", blog_posts = posts_list)

@app.route('/about')
def about():
    posts_data = Post()
    return render_template("about.html", blog_posts = posts_data)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/form-entry', methods=['GET','POST'])
def receive_data():
    if request.method == 'POST':
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['phone'])
        print(request.form['message'])
        
    return '<h1>Message Sent! {{name}} {{email}} {{phone}} {{message}}</h1>'

@app.route('/post/<number>')
def post(number):
    posts_data = Post()
    number =int(number)
    page = posts_data.get_blog(number)
    return render_template("post.html",page=page)



if __name__ == "__main__":
    app.run(debug=True)
