import numpy as np
import os.path as osp
from scipy.io import loadmat
from subprocess import call
from os import makedirs


subject_list = [1, 5, 6, 7, 8, 9, 11]
action_list = [x for x in range(2, 16)]
subaction_list = [x for x in range(1, 3)]
camera_list = [x for x in range(1, 5)]


from metadata import load_h36m_metadata
metadata = load_h36m_metadata()

makedirs('images', exist_ok=True)


cnt = 0
for s in subject_list:
    for a in action_list:
        for sa in subaction_list:
            for c in camera_list:
                subdir_format = 's_{:02d}_act_{:02d}_subact_{:02d}_ca_{:02d}'

                subdir = subdir_format.format(s, a, sa, c)
                makedirs(osp.join('images', subdir), exist_ok=True)

                fileformat = 'images' + '/' + subdir + '/' + subdir + '_%06d.jpg'

                basename = metadata.get_base_filename('S{:d}'.format(s), '{:d}'.format(a), '{:d}'.format(sa), metadata.camera_ids[c-1])
                videoname = basename + '.mp4'
                subject = 'S' + str(s)
                videopath = osp.join('extracted', subject, 'Videos', videoname)

                print(videopath)
                cnt += 1
                call([
                    'ffmpeg',
                    '-nostats',
                    '-i', videopath,
                    '-qscale:v', '3',
                    fileformat
                        ])




