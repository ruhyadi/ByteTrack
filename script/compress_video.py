"""Compress video with moviepy"""

import os
import moviepy.editor as mpy

def compress_video(input_file, output_file, bitrate='5000k'):
    """Compress video with moviepy"""
    clip = mpy.VideoFileClip(input_file)
    clip.write_videofile(output_file, bitrate=bitrate)

if __name__ == '__main__':
    compress_video(
        'YOLOX_outputs/yolox_s_mix_det/track_vis/2022_09_19_11_45_50/demo.mp4', 
        'YOLOX_outputs/yolox_s_mix_det/track_vis/2022_09_19_11_45_50/demo_compressed.mp4'
    )