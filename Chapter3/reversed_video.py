from moviepy.editor import VideoFileClip

def reverse_video(video_path, output_path):
    try:
        video = VideoFileClip(video_path)
        
        # Mengambil frame dari video dan membalikkan urutannya
        frames = [frame for frame in video.iter_frames()]
        reversed_frames = frames[::-1]
        
        # Membuat klip video dari frame yang dibalik
        reversed_video = video.set_duration(video.duration).fx(lambda clip: clip.set_make_frame(lambda t: reversed_frames[int((video.duration - t) * video.fps)]))
        
        # Menyimpan video yang telah dibalik
        reversed_video.write_videofile(output_path, codec='libx264', audio_codec='aac')
        
        print("Video berhasil dibalik dan disimpan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Panggil fungsi
reverse_video('example.mp4', 'reversed_result.mp4')