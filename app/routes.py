from app import app, db
from flask import render_template, url_for, redirect
from app.forms import ContactForm
from app.models import Contact
from flask import flash


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ContactForm()

    if form.validate_on_submit():
        try:
            contact = Contact(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                email = form.email.data,
                message = form.message.data
            )

            db.session.add(contact)
            db.session.commit()

            flash(f'Thanks for your submission, we will contact you shortly. A copy of the form has been sent to {form.email.data}')
            return redirect(url_for('index'))

        except:
            flash(f'Sorry your submission did not go through. Try again.   {form.first_name.data}')

            return redirect(url_for('index'))

    return render_template('index.html', form=form, title='Home')
