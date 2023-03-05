import os
INPUT_DIR = '../deep_sort/video-result'
OUTPUT_DIR = 'static/data/tracking-video'
for video in os.listdir(INPUT_DIR):
    input_path = os.path.join(INPUT_DIR, video)
    video_name = video.split('.')[0]
    output_path = os.path.join(OUTPUT_DIR, f'{video_name}.webm')
    os.system(f'ffmpeg -i {input_path} -c:v libvpx-vp9 -crf 30 -b:v 0 -b:a 128k -r 10 -c:a libopus {output_path}')