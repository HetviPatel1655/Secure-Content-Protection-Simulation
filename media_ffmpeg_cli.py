# “How do I extract audio/video streams from an MP4?”
# separate the audio-video file from the audio-video container using ffmpeg cli internally

import subprocess

def extract_streams(input_file, video_output, audio_output):
    # Extract video stream
    # Override output files if they exist
    # do not show ffmpeg output in console
    result = subprocess.run(['ffmpeg', '-y', '-i', input_file, '-c:v', 'copy', '-an', video_output],capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg error:\n{result.stderr}")

        # raise RuntimeError("FFmpeg failed to extract video stream.")
    
    # Extract audio stream
    # Override output files if they exist
    # skip if audio stream not present
    
    result = subprocess.run(['ffmpeg', '-y', '-i', input_file, '-c:a', 'copy', '-vn', audio_output], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg error:\n{result.stderr}")

        # raise RuntimeError("FFmpeg failed to extract audio stream.")
    
    #converting output files to string formats
    with open(video_output, 'rb') as vf:
        video_output = vf.read()
    with open(audio_output, 'rb') as af:
        audio_output = af.read()

    return video_output, audio_output

def merge_streams(video_input, audio_input, output_file):
    # Write video input to a temporary file
    with open('temp_video.h264', 'wb') as vf:
        vf.write(video_input)
    
    # Write audio input to a temporary file
    with open('temp_audio.aac', 'wb') as af:
        af.write(audio_input)
    
    # Merge video and audio streams
    result = subprocess.run(['ffmpeg', '-y', '-i', 'temp_video.h264', '-i', 'temp_audio.aac', '-c:v', 'copy', '-c:a', 'copy', output_file], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError("FFmpeg failed to merge streams.")
    
    # Clean up temporary files
    # subprocess.run(['rm', 'temp_video.h264', 'temp_audio.aac'])

    return output_file
