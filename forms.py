from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Playlist Name', validators=[InputRequired()])
    description = TextAreaField('Playlist Description', validators=[InputRequired()])

class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Song Title', validators=[InputRequired()])
    artist = StringField('Song Artist', validators=[InputRequired()])

class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
