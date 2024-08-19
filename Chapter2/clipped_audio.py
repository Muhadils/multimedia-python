from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('example.mp3')

# Pemotongan
clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('clipped_result.mp3', format='mp3')