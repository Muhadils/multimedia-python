from pydub import AudioSegment
import simpleaudio as sa

# Memuat file audio
audio = AudioSegment.from_file('example.mp3')
clipped_audio = AudioSegment.from_file('originalsound.mp3')

# Penggabungan
combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')