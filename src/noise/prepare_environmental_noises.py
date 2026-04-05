
import os
import librosa
import soundfile as sf

def audio2_level(audio2_path):
    level = 1
    its_wind = False

    if audio2_path == 'Birds.wav':
        level = 0.1
    elif audio2_path == 'Car_engine_pass.wav':
        level = 0.1
    elif audio2_path == 'Car_horn.wav':
        level = 0.1
    elif audio2_path == 'Cat.wav':
        level = 0.1
    elif audio2_path == 'Church_bell.wav':
        level = 0.1
    elif audio2_path == 'Clock_tick.wav':
        level = 1
    elif audio2_path == 'Dog.wav':
        level = 1
    elif audio2_path == 'Fan.wav':
        level = 0.5
    elif audio2_path == 'Music.wav':
        level = 0.1
    elif audio2_path == 'Office_chair_sitting_down.wav':
        level = 1
    elif audio2_path == 'Placing_objects_on_desk.wav':
        level = 1
    elif audio2_path == 'Radio_danish.wav':
        level = 0.5
    elif audio2_path == 'Raindrops_on_window.wav':
        level = 1.5
    elif audio2_path == 'Siren.wav':
        level = 0.1
    elif audio2_path == 'Talking_english.wav':
        level = 0.5
    elif audio2_path == 'Thunder_rain.wav':
        level = 0.05
    elif audio2_path == 'TV.wav':
        level = 1
    elif audio2_path == 'Wind_window.wav':
        level = 1
        its_wind = True
    elif audio2_path == 'Wooden_door_open_close.wav':
        level = 1

    return level, its_wind

def prepare_noises(input_path, output_path, sr=44100, duration=5.0):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for filename in os.listdir(input_path):
        if filename.endswith('.wav'):
            level, its_wind = audio2_level(filename)

            if its_wind:
                audio, sr = librosa.load(os.path.join(input_path, filename), sr=sr, offset=6.0, duration=duration)
            else:
                audio, sr = librosa.load(os.path.join(input_path, filename), sr=sr, duration=duration)

            new_audio = audio[:int(sr * duration)] * level
            sf.write(os.path.join(output_path, filename), new_audio, sr)
