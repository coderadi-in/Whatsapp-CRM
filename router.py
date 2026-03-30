'''coderadi &bull; Routes management file for the project.'''

# ? IMPORTS
from flask import Blueprint, render_template, redirect, url_for, request
from plugins import *

# ! INITIALIZATION
router = Blueprint('router', __name__)
twilio_num = os.getenv("TWILIO_NUM")

# & HOME
@router.route('/')
def home():
    return render_template('home.html')

# & WEBHOOK
@router.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.form.get("body")
    sender = request.form.get("from")

    print(incoming_msg)
    reply = "Got your message. Will get back shortly."

    client.messages.create(
        from_=f'whatsapp:{twilio_num}',
        body=reply,
        to=f'whatsapp:{sender}'
    )

    new_message = Message(
        body=incoming_msg,
        sender=sender
    )

    db.session.add(new_message)
    db.session.commit()

    return redirect(url_for('router.home'))

# & DB
@router.route('/db')
def show_db():
    data = Message.query.all()
    return render_template('db.html', data=data)