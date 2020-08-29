import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'
app.config['MAIL_SERVER'] = os.environ.get('SMTP_HOSTNAME')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        recipient = request.form['recipient']
        msg = Message('Primeiros passos com Docker', recipients=[recipient])
        msg.body = ('Essa mensagem foi enviada pelo container de disparo de e-mail!')
        msg.html = ('<h1>Primeiros passos com Docker</h1>'
                    '<p>Você está aprendendo como criar um '
                    '<b>ambiente containerizado</b>!</p>')
        mail.send(msg)
        flash(f'Mensagem enviada para {recipient}.')
        return redirect(url_for('index'))
    return render_template('index.html')

