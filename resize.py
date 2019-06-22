from PIL import Image
import sys
import os
import json
import traceback
from datetime import datetime

MANIFEST_PATH = './resize_manifest.json'
DIST_DIR = './dist'


def main(base_image_path):
    if os.path.exists(base_image_path) is False:
        print('"{}" does not exists.'.format(base_image_path))
        return False

    manifest_data = get_manifest_data()
    if manifest_data is False:
        return False

    process_ts = str(datetime.now().strftime('%s'))
    dist_dir = '{}/{}'.format(DIST_DIR, process_ts)
    os.mkdir(dist_dir)
    if os.path.exists(dist_dir) is False:
        print('Failed to create dist directly.')
        return False

    base_file_object = Image.open(base_image_path)
    for manifest in manifest_data:
        resize_image(base_file_object, manifest, dist_dir)


def resize_image(base_file_object, manifest, dist_dir):
    try:
        if 'alpha' in manifest and manifest['alpha'] is False:
            base_file_object = base_file_object.convert('RGB')
        img_resize = base_file_object.resize(
            (manifest['x'], manifest['y']), Image.LANCZOS)
        img_resize.save('{}/{}'.format(dist_dir, manifest['name']))
    except Exception:
        print(traceback.format_exc())
        print('Failed to resize to "{}" sized {} x {}.'.format(
            manifest['name'], manifest['x'], manifest['y']))
        return False


def get_manifest_data():
    if os.path.exists(MANIFEST_PATH) is False:
        print('"resize_manifest.json" does not exists.')
        return False

    try:
        f = open(MANIFEST_PATH, 'r')
        manifest_data = json.load(f)
        return manifest_data
    except Exception:
        print(traceback.format_exc())
        print('An error occuerd at loading manifest data.')
        return False


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print('First argument for base image file path is required.')
        quit()

    print(args[1])
    main(args[1])
