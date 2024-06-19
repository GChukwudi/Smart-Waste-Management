from flask import render_template, flash, redirect, url_for, request
from app import db
from app.forms import LoginForm, RegistrationForm, ScheduleForm
from app.models import User, Schedule
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse  # Corrected import
from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Home')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@bp.route('/schedule', methods=['GET', 'POST'])
@login_required
def schedule():
    form = ScheduleForm()
    if form.validate_on_submit():
        schedule = Schedule(date=form.date.data, time=form.time.data, user_id=current_user.id)
        db.session.add(schedule)
        db.session.commit()
        flash('Your waste collection schedule has been set!')
        return redirect(url_for('main.index'))
    return render_template('schedule.html', title='Schedule', form=form)
