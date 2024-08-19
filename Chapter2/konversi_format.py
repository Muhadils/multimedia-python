from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('example.mp3')

# Konversi Format
audio.export('result.wav', format='wav')