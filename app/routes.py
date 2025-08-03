from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignupForm, LoginForm, AccessWealthPaymentForm, LogoutForm, PaymentForm
from flask_login import current_user, login_user, logout_user
from app.models import User
from app import db
from app.payload import generate_payfast_payload

@app.route("/")
@app.route("/index")
def index():
    logout_form = LogoutForm()
    return render_template('index.html', logout_form=logout_form)

@app.route('/accesswealth')
def accesswealth():
    return render_template('accesswealth.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data
        )
        
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('payment'))
        else:
            flash('Login failed. Check your email and password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout', methods=['POST'])
def logout():
   if current_user.is_authenticated:
        logout_user()
        flash('You have been logged out.', 'success')
        return redirect(url_for('index'))

@app.route('/accesswealth/payment', methods=['GET', 'POST'])
def accesswealth_payment():
    form = AccessWealthPaymentForm()
    if form.validate_on_submit():
        
        flash('Payment successful! Welcome to AccessWealth.', 'success')
        return redirect(url_for('payment'))
    return render_template('accesswealth_payment.html', form=form)

@app.route('/payment', methods=['GET', 'POST'])
@login_required
def payment():
    form = PaymentForm()
    if form.validate_on_submit():
        payload = generate_payfast_payload(form)
        payfast_url = app.config.get('PAYFAST_URL', 'https://www.payfast.co.za/eng/process')
        return render_template('payfast_redirect.html', payload=payload, payfast_url=payfast_url)


        flash('Payment successful! Thank you for your purchase.', 'success')
        return redirect(url_for('index'))
    return render_template('payment.html', form=form)

