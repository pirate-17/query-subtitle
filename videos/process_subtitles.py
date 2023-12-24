import subprocess
import os
import pysrt

# get the video
def extract_subtitles(media_dir, file_name):

    file_path = os.path.join(media_dir, file_name)
    cmd = f'ccextractor {file_path}'
    subprocess.run(cmd, shell=True)

    subtitle_file_name = file_path.strip().split('.')[0] + '.srt'
    return subtitle_file_name


def search_keyword_in_subtitles(st_file, keyword):
    # search keywords in the subtitle file

    subs = pysrt.open(st_file)

    for sub in subs:
        if keyword in sub.text.lower():
            start_time = sub.start.to_time()
            end_time = sub.end.to_time()
            return f"Keyword {keyword} found in time phrase {start_time} --> {end_time}"
    return f"Keyword {keyword} not found in the subtitle file"



def upload_to_dynamoDB():
    # upload the subtitle file to dynamoDB
    pass