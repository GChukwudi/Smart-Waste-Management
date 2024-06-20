from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, ScheduleForm, RecyclingForm, ImpactMetricForm
from app.models import User, Schedule, Recycling, ImpactMetric, MaterialRecycled
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from collections import defaultdict


main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('index.html')

@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')

@main.route("/schedule", methods=['GET', 'POST'])
@login_required
def schedule():
    form = ScheduleForm()
    if form.validate_on_submit():
        schedule = Schedule(date=form.date.data, author=current_user)
        db.session.add(schedule)
        db.session.commit()
        flash('Your schedule has been created!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('schedule.html', title='Schedule', form=form)


@main.route("/recycle", methods=['GET', 'POST'])
@login_required
def recycle():
    form = RecyclingForm()
    if form.validate_on_submit():
        recycling = Recycling(materials=form.materials.data, date_posted=datetime.utcnow(), author=current_user)
        db.session.add(recycling)
        db.session.commit()
        flash('Your recycling effort has been logged!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('recycle.html', title='Recycle', form=form)

@main.route("/user/<username>")
@login_required
def user_profile(username):
    user = User.query.filter_by(username=username).first_or_404()

    material_to_increment = request.args.get('material')
    if material_to_increment:
        material_recycled = MaterialRecycled.query.filter_by(user_id=user.id, material=material_to_increment).first()
        if material_recycled:
            material_recycled.count += 1
        else:
            material_recycled = MaterialRecycled(material=material_to_increment, count=1, user_id=user.id)
            db.session.add(material_recycled)
        db.session.commit()

    return render_template('user_profile.html', title='User Profile', user=user)


@main.route("/track", methods=['GET', 'POST'])
@login_required
def track():
    form = ImpactMetricForm()
    if form.validate_on_submit():
        impact = ImpactMetric(carbon_saved=form.carbon_saved.data, energy_saved=form.energy_saved.data, author=current_user)
        db.session.add(impact)
        db.session.commit()
        flash('Your environmental impact has been tracked!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('track.html', title='Track Impact', form=form)

@main.route("/admin")
@login_required
def admin():
    if current_user.role != 'admin':
        return redirect(url_for('main.home'))
    users = User.query.all()
    schedules = Schedule.query.all()
    recyclings = Recycling.query.all()
    impacts = ImpactMetric.query.all()
    return render_template('admin.html', title='Admin Dashboard', users=users, schedules=schedules, recyclings=recyclings, impacts=impacts)
