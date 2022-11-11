import moviepy.editor as mp

my_clip = mp.VideoFileClip(r"C:\Users\Asus\Videos\iTubeGo\Download\How to Give a 60 Second Self-Introduction Presentation.mp4")

my_clip.audio.write_audiofile(r"my_result.mp3")
