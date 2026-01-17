# Check if the video file contains both video and audio streams 

def check_streams(file_name, media_ffmpeg_cli):
    has_video = media_ffmpeg_cli.has_video_stream(file_name)
    has_audio = media_ffmpeg_cli.has_audio_stream(file_name)
    return has_video and has_audio