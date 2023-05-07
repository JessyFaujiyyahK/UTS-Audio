from flask import Flask, render_template, request, jsonify, send_from_directory #framework web python, membuat template HTML, mengakses data, mengirim data JSON, mengirim file statis
import os #mengatur path
from werkzeug.utils import secure_filename #mengamankan nama file
from pydub import AudioSegment #kompres

app = Flask(__name__) #membuat aplikasi flask
app.config['UPLOAD_FOLDER'] = 'static' #path


@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files: #jika tidak terdapat 'file' maka akan error
        return jsonify({'error': 'No file part'})
    
    audio_file = request.files['file']
    filename = secure_filename(audio_file.filename) #membuat nama file yang aman
    new_filename = 'before.mp3'
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
    
    if os.path.isfile(filepath): #menggunakan nama yang sudah ada maka file sebelumnya dihapus
        os.remove(filepath)

    # Save the file
    audio_file.save(filepath)
    
    mainAudio = AudioSegment.from_mp3("static/before.mp3") #memuat file audio
    audio1 = AudioSegment.from_mp3("effect/explosion.mp3")
    audio2 = AudioSegment.from_mp3("effect/applause.mp3")
    audio3 = AudioSegment.from_mp3("effect/minion.mp3")
    audio4 = AudioSegment.from_mp3("effect/gunshot.mp3")
    audio5 = AudioSegment.from_mp3("effect/GlassFalls.mp3")
    audio6 = AudioSegment.from_mp3("effect/Plane.mp3")
    audio7 = AudioSegment.from_mp3("effect/Thunder.mp3")
    audio8 = AudioSegment.from_mp3("effect/wind.mp3")
    audio9 = AudioSegment.from_mp3("effect/LionGrowlAngry.mp3")
    audio10 = AudioSegment.from_mp3("effect/PoliceSiren.mp3")    
    a = request.form.get('audio') #mengambil nilai dari form select

    if a == '1':
        mixed_audio = mainAudio.overlay(audio1 - 10) #mixed, dikurang 10 decibels

    elif a == '2':
        mixed_audio = mainAudio.overlay(audio2 - 10)

    elif a == '3':
        mixed_audio = mainAudio.overlay(audio3 - 10)

    elif a == '4':
        mixed_audio = mainAudio.overlay(audio4 - 10)

    elif a == '5':
        mixed_audio = mainAudio.overlay(audio5 - 10)
    
    elif a == '6':
        mixed_audio = mainAudio.overlay(audio6 - 10)
    
    elif a == '7':
        mixed_audio = mainAudio.overlay(audio7 - 10)

    elif a == '8':
        mixed_audio = mainAudio.overlay(audio8 - 10)
    
    elif a == '9':
        mixed_audio = mainAudio.overlay(audio9 - 10)
    
    elif a == '10':
        mixed_audio = mainAudio.overlay(audio10 - 10)
    
    mixed_path = os.path.join(app.config['UPLOAD_FOLDER'], 'after.mp3')

    mixed_audio = mixed_audio.set_frame_rate(22050) #setelah di mix 22050 Hz, kualitas baik ukuran file cukup kecil
    mixed_audio = mixed_audio.set_sample_width(2) #untuk mempresentasikan setiap sampel audio, nilai 2 byte
    mixed_audio = mixed_audio.set_channels(1) #mudah dikontrol dalam hal pengaturan volume dan kualitas suara di web
    mixed_audio.export(mixed_path, format='mp3', bitrate='96k') #untuk mengkompress pake bitrate 96k -> standar bitrate

    return render_template('play.html', after=mixed_audio)

if __name__ == '__main__':
    app.run(debug=True)
