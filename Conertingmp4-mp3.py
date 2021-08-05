from moviepy.editor import *

mp4File = 'VideoFile.mp4'

mp3File = 'AudioFile.mp3'

videoClip = VideoFileClip(mp4File)

audioclip = videoClip.audio

audioclip.write_audiofile(mp3File)

audioclip.close()
videoClip.close()