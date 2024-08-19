from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('example.mp3')

# Pengaturan Volume
louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder_result.mp3', format='mp3')