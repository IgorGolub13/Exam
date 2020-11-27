



from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class AddAudioForm(FlaskForm):
    title = StringField('Title', validators=[Length(min=4, max=30,
                                              message='Це поле має бути довжиною між 4 та 25 символів'),
                                       DataRequired(message='Це поле обовязкове')])
    class_music = StringField('Set class of audio.', validators=[Length(min=4, max=30,
                                              message='Це поле має бути довжиною між 4 та 25 символів'),
                                       DataRequired(message='Це поле обовязкове')])
    singer = StringField('Set autor of audio.',  validators=[Length(min=4, max=30,
                                              message='Це поле має бути довжиною між 4 та 25 символів'),
                                       DataRequired(message='Це поле обовязкове')])
    describe = TextAreaField('Describe the song.')
    length = StringField('Set length of audio.', validators=[DataRequired(message='Це поле обовязкове')])
    data_type = StringField('Set type of audio.', validators=[DataRequired(message='Це поле обовязкове')])
    rating_ball = StringField('Set rating of audio.', validators=[DataRequired(message='Це поле обовязкове')])
    submit = SubmitField('Add audio')



