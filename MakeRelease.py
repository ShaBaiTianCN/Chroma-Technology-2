import os
import shutil
import zipfile

import requests

PROJECT_NAME = 'Chroma-Technology-2'
PACK_VERSION = '1.2.1'

RESOURCES_PACK_URL = 'https://gitee.com/api/v5/repos/ShaBaiTianCN/Minecraft-Mod-Language-Package-Not-Included-Language-Package/releases/latest'

VERSION = input('Version: ')
RELEASE_NAME = '-'.join([VERSION, '汉化补丁', PROJECT_NAME, PACK_VERSION])
RELEASE_DIR = os.path.join('temp', RELEASE_NAME)


def touch_dir(path: str):
    """
    Create folder if not exist.
    :param path: Folder path.
    """
    if not os.path.isdir(path):
        os.makedirs(path)


def copy(file_path: str, check_dir: bool = True):
    """
    Copy file to release folder.
    :param file_path: File path.
    :param check_dir: Enable check dir exist.
    """
    target_path = os.path.join(RELEASE_DIR, file_path)
    if check_dir:
        touch_dir(os.path.dirname(target_path))
    shutil.copyfile(file_path, target_path)


def main():
    # Touch folder
    touch_dir(RELEASE_DIR)

    # Copy file
    for dirpath, dirnames, filenames in os.walk('.'):
        if '.git' in dirpath or 'temp' in dirpath or '.idea' in dirpath:
            continue
        for filename in filenames:
            if dirpath == '.' and filename in ['.gitignore', 'MakeRelease.py']:
                continue
            elif filename == 'en_us.json':
                continue
            else:
                file_path = os.path.join(dirpath, filename)
                copy(file_path)

    # Download resource pack
    release_info = requests.get(RESOURCES_PACK_URL).json()['assets'][0]
    resourcepack_dir = os.path.join(RELEASE_DIR, 'resourcepacks')
    resourcepack_path = os.path.join(resourcepack_dir, release_info['name'])
    touch_dir(resourcepack_dir)
    with open(resourcepack_path, 'wb') as f:
        f.write(requests.get(release_info['browser_download_url']).content)

    # Make Zipfile
    with zipfile.ZipFile(
            f'{RELEASE_DIR}.zip',
            mode='w',
            compression=zipfile.ZIP_DEFLATED
    ) as archive:
        for dirpath, dirnames, filenames in os.walk(RELEASE_DIR):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                archive.write(
                    file_path,
                    arcname=file_path.replace(RELEASE_DIR, '')
                )

    # Remove folder
    shutil.rmtree(RELEASE_DIR)


if __name__ == '__main__':
    main()
