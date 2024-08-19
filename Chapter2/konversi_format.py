from pydub import AudioSegment
import simpleaudio as sa

# Memuat file audio
audio = AudioSegment.from_file('example.mp3')

# Konversi Format
audio.export('result.wav', format='wav')