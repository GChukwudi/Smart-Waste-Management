from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, ScheduleForm, RecyclingForm, ImpactMetricForm, TrackForm
from app.models import User, Schedule, Recycling, ImpactMetric
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from collections import defaultdict
# import json


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
    impact_metrics = ImpactMetric.query.filter_by(user=current_user).all()
    schedules = Schedule.query.filter_by(user=current_user).all()
    recyclings = Recycling.query.filter_by(user=current_user).all()

    labels = [impact.date_tracked.strftime('%Y-%m-%d') for impact in impact_metrics]
    carbon_saved = [impact.carbon_saved for impact in impact_metrics]
    energy_saved = [impact.energy_saved for impact in impact_metrics]

    impact_data = {
        'labels': labels,
        'carbon_saved': carbon_saved,
        'energy_saved': energy_saved
    }

    return render_template('dashboard.html', title='Dashboard', impact_data=impact_data, schedules=schedules, recyclings=recyclings)


@main.route("/schedule", methods=['GET', 'POST'])
@login_required
def schedule():
    form = ScheduleForm()
    if form.validate_on_submit():
        schedule = Schedule(date=form.date.data, user=current_user)
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
        recycling = Recycling(materials_recycled=form.materials.data, date_posted=datetime.utcnow(), user=current_user)
        db.session.add(recycling)
        db.session.commit()
        flash('Your recycling effort has been logged!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('recycle.html', title='Recycle', form=form)

@main.route("/user/<username>")
@login_required
def user_profile(username):
    user = User.query.get_or_404(current_user.id)
    user_materials_recycled = defaultdict(int)
    for item in user.recyclings:
        user_materials_recycled[item.materials_recycled] += 1
    return render_template('user_profile.html', user=user, materials_recycled=dict(user_materials_recycled))

@main.route('/track', methods=['GET','POST'])
@login_required  # Assuming you use Flask-Login
def track():
    form = TrackForm()
    if form.validate_on_submit():
        carbon_saved = form.carbon_saved.data
        energy_saved = form.energy_saved.data
        
        # Ensure current_user is imported correctly
        impact = ImpactMetric(
            carbon_saved=carbon_saved,
            energy_saved=energy_saved,
            date_tracked=datetime.now(),
            user_id=current_user.id  # Assuming current_user has an 'id' attribute
        )
        
        db.session.add(impact)
        db.session.commit()
        flash('Impact metrics logged successfully!', 'success')
        return redirect(url_for('main.track'))
    
    impact_metrics = ImpactMetric.query.all()
    return render_template('track.html', title='Track Impact', form=form, impact_metrics=impact_metrics)

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
