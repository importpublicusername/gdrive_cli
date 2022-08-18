"""restores all items currently in the trash"""

#expects a client_secrets.json file to be downloaded from your google apis 
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

from loguru import logger

def main():
    """restores all items currently in the trash"""
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

    logger.info('getting list')
    file_list = drive.ListFile({'q': "trashed = true"}).GetList()
    length = len(file_list)
    logger.info(f'have the list: {length}')
    for file in file_list:
        title = file['title']
        id = file['id']
        logger.debug(f'title: {title}, id: {id}')
        file.UnTrash()
        length -= 1
        if length % 25 == 0:
            logger.info(f'remaining: {length}')

if __name__ == "__main__":
    main()
