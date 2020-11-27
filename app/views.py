





from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.forms import AddAudioForm
from app.models import Audio
from werkzeug.urls import url_parse
import os
import secrets
from datetime import datetime as dt

@app.route('/add_audio', methods=['GET', 'POST'])
def add_audio():
    form = AddAudioForm()
    if form.validate_on_submit():
        title = form.title.data
        class_music = form.class_music.data
        singer = form.singer.data
        describe = form.describe.data
        length = form.length.data
        data_type = form.data_type.data
        rating_ball = form.rating_ball.data
        date_posted = dt.utcnow()
        audio = Audio(title=title, class_music=class_music, singer=singer, describe=describe, length=length,
                      data_type=data_type, rating_ball=rating_ball, date_posted=date_posted)
        db.session.add(audio)
        db.session.commit()
        flash('New audio added!', category='success')
        return redirect(url_for('audios'))
    return render_template('add_audio.html', form=form)


@app.route('/audios', methods=['GET', 'POST'])
def audios():
    audios = Audio.query.all()
    return render_template("audios.html", title='Audios', audios=audios)

@app.route('/')
def index():
    return render_template('index.html')