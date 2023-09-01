from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import InputRequired, URL
from dictionary import el_principito_1, el_principito_2, chapter_1, chapter_2
import os
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from pydub import AudioSegment
from io import BytesIO
import time
from datetime import datetime

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"

# ------------------------------------------------------ VARIABLES ----------------------------------------------------#
time_sec = time.localtime()
current_year = time_sec.tm_year
# getting the current date and time
current_datetime = datetime.now()
# getting the time from the current date and time in the given format
current_time = current_datetime.strftime("%a %d %B")


# -------------------------------------------------------- CLASS ------------------------------------------------------#
class UrlForm(FlaskForm):
    user_input = URLField('€nter the URL(book, text... .) below:',
                          validators=[InputRequired(message="Please enter text."),
                                      URL(message="Please enter a valid URL.")])
    submit = SubmitField()


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


# Set AWS credentials
# Retrieve AWS credentials and region from environment variables
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
region_name = os.environ.get('AWS_REGION', 'eu-west-1')  # Default to 'eu-west-1' if AWS_REGION is not set

polly = boto3.client('polly', region_name=region_name, aws_access_key_id=aws_access_key_id,
                     aws_secret_access_key=aws_secret_access_key)


# Function to synthesize speech with a specified voice accent
# Function to synthesize speech with a specified voice accent
def synthesize_speech(text, voice_id='Joanna'):
    try:
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId=voice_id  # Default to Joanna (English accent)
        )

        # Get audio data from Polly response
        audio_data = response['AudioStream'].read()

        return AudioSegment.from_mp3(BytesIO(audio_data))

    except (BotoCoreError, ClientError) as e:
        print(f"Error synthesizing speech with Polly: {str(e)}")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None


@app.route('/', methods=['GET', 'POST'])
def home():
    user_input_form = UrlForm()
    preface = el_principito_1['chapter 1']

    if request.method == "POST" and user_input_form.validate_on_submit():
        user_input_data = user_input_form.user_input.data.strip()
        print(f'URL: {user_input_data}')
    return render_template('audiobook.html', year=current_year, date=current_time, preface=preface,
                           user_input_form=user_input_form)


@app.route('/el-principito1')  # Define a unique URL path for el_principito1 audio
def el_principito1():
    # Initialize an empty audiobook
    audiobook = AudioSegment.empty()

    # Iterate through the dictionary and generate speech for el_principito1
    for chapter_title, chapter_text in el_principito_1.items():
        # Use 'Conchita' (Spanish accent) for the voice accent
        chapter_audio = synthesize_speech(chapter_text, voice_id='Conchita')
        if chapter_audio:
            audiobook += chapter_audio

    # Export the audiobook to an in-memory buffer
    audio_buffer = BytesIO()
    audiobook.export(audio_buffer, format='mp3')
    audio_buffer.seek(0)

    return audio_buffer.read(), 200, {'Content-Type': 'audio/mpeg'}


@app.route('/el-principito2')  # Define a unique URL path for el_principito2 audio
def el_principito2():
    # Initialize an empty audiobook
    audiobook = AudioSegment.empty()

    # Iterate through the dictionary and generate speech for el_principito1
    for chapter_title, chapter_text in el_principito_2.items():
        # Use 'Conchita' (Spanish accent) for the voice accent
        chapter_audio = synthesize_speech(chapter_text, voice_id='Conchita')
        if chapter_audio:
            audiobook += chapter_audio

    # Export the audiobook to an in-memory buffer
    audio_buffer = BytesIO()
    audiobook.export(audio_buffer, format='mp3')
    audio_buffer.seek(0)

    return audio_buffer.read(), 200, {'Content-Type': 'audio/mpeg'}


@app.route('/el-principito3')  # Define a unique URL path for el_principito1 audio
def el_principito3():
    # Initialize an empty audiobook
    audiobook = AudioSegment.empty()

    # Iterate through the dictionary and generate speech for el_principito1
    for chapter_title, chapter_text in el_principito_1.items():
        # Use 'Conchita' (Spanish accent) for the voice accent
        chapter_audio = synthesize_speech(chapter_text, voice_id='Conchita')
        if chapter_audio:
            audiobook += chapter_audio

    # Export the audiobook to an in-memory buffer
    audio_buffer = BytesIO()
    audiobook.export(audio_buffer, format='mp3')
    audio_buffer.seek(0)

    return audio_buffer.read(), 200, {'Content-Type': 'audio/mpeg'}


@app.route('/el-principito4')  # Define a unique URL path for el_principito1 audio
def el_principito4():
    # Initialize an empty audiobook
    audiobook = AudioSegment.empty()

    # Iterate through the dictionary and generate speech for el_principito1
    for chapter_title, chapter_text in el_principito_1.items():
        # Use 'Conchita' (Spanish accent) for the voice accent
        chapter_audio = synthesize_speech(chapter_text, voice_id='Conchita')
        if chapter_audio:
            audiobook += chapter_audio

    # Export the audiobook to an in-memory buffer
    audio_buffer = BytesIO()
    audiobook.export(audio_buffer, format='mp3')
    audio_buffer.seek(0)

    return audio_buffer.read(), 200, {'Content-Type': 'audio/mpeg'}


@app.route('/el-principito5')  # Define a unique URL path for el_principito1 audio
def el_principito5():
    # Initialize an empty audiobook
    audiobook = AudioSegment.empty()

    # Iterate through the dictionary and generate speech for el_principito1
    for chapter_title, chapter_text in el_principito_1.items():
        # Use 'Conchita' (Spanish accent) for the voice accent
        chapter_audio = synthesize_speech(chapter_text, voice_id='Conchita')
        if chapter_audio:
            audiobook += chapter_audio

    # Export the audiobook to an in-memory buffer
    audio_buffer = BytesIO()
    audiobook.export(audio_buffer, format='mp3')
    audio_buffer.seek(0)

    return audio_buffer.read(), 200, {'Content-Type': 'audio/mpeg'}


@app.route('/el-principito6')  # Define a unique URL path for el_principito1 audio
def el_principito6():
    # Initialize an empty audiobook
    audiobook = AudioSegment.empty()

    # Iterate through the dictionary and generate speech for el_principito1
    for chapter_title, chapter_text in el_principito_1.items():
        # Use 'Conchita' (Spanish accent) for the voice accent
        chapter_audio = synthesize_speech(chapter_text, voice_id='Conchita')
        if chapter_audio:
            audiobook += chapter_audio

    # Export the audiobook to an in-memory buffer
    audio_buffer = BytesIO()
    audiobook.export(audio_buffer, format='mp3')
    audio_buffer.seek(0)

    return audio_buffer.read(), 200, {'Content-Type': 'audio/mpeg'}


@app.route('/el-principito7')  # Define a unique URL path for el_principito1 audio
def el_principito7():
    # Initialize an empty audiobook
    audiobook = AudioSegment.empty()

    # Iterate through the dictionary and generate speech for el_principito1
    for chapter_title, chapter_text in el_principito_1.items():
        # Use 'Conchita' (Spanish accent) for the voice accent
        chapter_audio = synthesize_speech(chapter_text, voice_id='Conchita')
        if chapter_audio:
            audiobook += chapter_audio

    # Export the audiobook to an in-memory buffer
    audio_buffer = BytesIO()
    audiobook.export(audio_buffer, format='mp3')
    audio_buffer.seek(0)

    return audio_buffer.read(), 200, {'Content-Type': 'audio/mpeg'}


@app.route('/miserable-chapter1')  # Define a unique URL path for miserable_chapter1 audio
def miserable_chapter1():
    # Initialize an empty audiobook
    audiobook = AudioSegment.empty()

    # Iterate through the dictionary and generate speech for miserable_chapter1
    for chapter_title, chapter_text in chapter_1.items():
        chapter_audio = synthesize_speech(chapter_text, voice_id='Salli')  # Use 'Salli' voice accent
        if chapter_audio:
            audiobook += chapter_audio

    # Export the audiobook to an in-memory buffer
    audio_buffer = BytesIO()
    audiobook.export(audio_buffer, format='mp3')
    audio_buffer.seek(0)

    return audio_buffer.read(), 200, {'Content-Type': 'audio/mpeg'}


@app.route('/miserable-chapter2')  # Define a unique URL path for miserable_chapter2 audio
def miserable_chapter2():
    # Initialize an empty audiobook
    audiobook = AudioSegment.empty()

    # Iterate through the dictionary and generate speech for miserable_chapter2
    for chapter_title, chapter_text in chapter_2.items():
        chapter_audio = synthesize_speech(chapter_text)
        if chapter_audio:
            audiobook += chapter_audio

    # Export the audiobook to an in-memory buffer
    audio_buffer = BytesIO()
    audiobook.export(audio_buffer, format='mp3')
    audio_buffer.seek(0)

    return audio_buffer.read(), 200, {'Content-Type': 'audio/mpeg'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
