# “How do I extract audio/video streams from an MP4?”
# separate the audio-video file from the audio-video container using ffmpeg cli internally

import subprocess

def check_streams(file_name):
    has_video = int(has_video_stream(file_name))
    has_audio = int(has_audio_stream(file_name))
    print(f"File: {file_name} | Video Stream: {has_video} | Audio Stream: {has_audio}")
    print("Type of has_audio:", type(has_audio))

    return has_video , has_audio

def has_video_stream(file_name):
    result = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=index', '-of', 'csv=p=0', file_name], capture_output=True, text=True)
    print(result.stdout.strip())
    return result.stdout.strip() != ''

def has_audio_stream(file_name):
    result = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'a', '-show_entries', 'stream=index', '-of', 'csv=p=0', file_name], capture_output=True, text=True)
    print(result.stdout.strip())
    return result.stdout.strip() != ''
    

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
    
    if not has_audio_stream(input_file):
        with open(audio_output, 'wb') as af:
            af.write(b'')
    else:
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

# def merge_streams(video_input, audio_input, output_file):
#     # Write video input to a temporary file
#     with open('temp_video.h264', 'wb') as vf:
#         vf.write(video_input)
    
#     # Write audio input to a temporary file
#     with open('temp_audio.aac', 'wb') as af:
#         af.write(audio_input)
    
#     # Merge video and audio streams
#     result = subprocess.run(['ffmpeg', '-y', '-i', 'temp_video.h264', '-i', 'temp_audio.aac', '-c:v', 'copy', '-c:a', 'copy', output_file], capture_output=True, text=True)
#     if result.returncode != 0:
#         raise RuntimeError("FFmpeg failed to merge streams.")
    
#     # Clean up temporary files
#     # subprocess.run(['rm', 'temp_video.h264', 'temp_audio.aac'])

#     return output_file

def merge_streams(video_input, audio_input, output_file):
    # Write video input to a temporary file (Always required)
    with open('temp_video.h264', 'wb') as vf:
        vf.write(video_input)
    
    # Base command: Input video and copy video codec
    cmd = ['ffmpeg', '-y', '-i', 'temp_video.h264']
    
    # CHECK: Only process audio if data exists and is not empty
    if audio_input and len(audio_input) > 0:
        # Write audio to temp file
        with open('temp_audio.aac', 'wb') as af:
            af.write(audio_input)
            
        # Add audio input and mapping to command
        cmd.extend(['-i', 'temp_audio.aac', '-c:v', 'copy', '-c:a', 'copy', output_file])
    else:
        # No audio: Just copy video stream to output
        # (Using -c:v copy ensures we don't re-encode)
        cmd.extend(['-c:v', 'copy', output_file])

    # Run the constructed command
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        # Print stderr to help debug if it fails again
        print(f"FFmpeg Error Details: {result.stderr}")
        raise RuntimeError("FFmpeg failed to merge streams.")

    # Cleanup (Optional: distinct cleanup for audio file if it exists)
    # if os.path.exists('temp_video.h264'): os.remove('temp_video.h264')
    # if os.path.exists('temp_audio.aac'): os.remove('temp_audio.aac')

    return output_file