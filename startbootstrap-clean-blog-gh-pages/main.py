from flask import Flask, render_template, request
from post import Post
import smtplib
from email_config import email

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

@app.get('/contact')
def contact():
    return render_template("contact.html")

@app.post('/contact')
def get_contact():
    name =request.form['name']
    email =request.form['email']
    phone =request.form['phone']
    message =request.form['message']
    
    email_text = {
        'name':name,
        'phone':phone,
        'email':email,
        'message':message,
    }
    text = ''
    for key, value in email_text.items():
        text += f'{key} : {value},\n'
    
    print(text)
    send_email(text)
    
    success_message = 'Message Sent!'
    
    return render_template('contact.html', message=success_message)

def send_email(message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email['address'], password=email['password'])
        connection.sendmail(from_addr=email['address'], to_addrs=email['address'], msg=message)
        print(message)


# @app.route('/', methods=['GET','POST'])
# def receive_data():
#     if request.method == 'POST':
#         print(request.form['name'])
#         print(request.form['email'])
#         print(request.form['phone'])
#         print(request.form['message'])
        
#     return '<h1>Message Sent!</h1>'

@app.route('/post/<number>')
def post(number):
    posts_data = Post()
    number =int(number)
    page = posts_data.get_blog(number)
    return render_template("post.html",page=page)



if __name__ == "__main__":
    app.run(debug=True)
