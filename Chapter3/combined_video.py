from moviepy.editor import VideoFileClip, concatenate_videoclips

# Memuat file video
video = VideoFileClip('example.mp4')
short_video = VideoFileClip('short_result.mp4')

# Penggabungan
combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')