from moviepy.editor import VideoFileClip, vfx

# Memuat file video
short_video = VideoFileClip('short_result.mp4')

# Pengaturan Kecepatan
sped_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
sped_up_video.write_videofile('sped_up_result.mp4')