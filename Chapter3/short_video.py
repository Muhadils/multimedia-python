from moviepy.editor import VideoFileClip

# Memuat file video
video = VideoFileClip('example.mp4')

# Pemotongan
short_video = video.subclip(0, 10)  # Mendapatkan 10 detik pertama
short_video.write_videofile('short_result.mp4')