#expects a client_secrets.json file to be downloaded from your google apis 
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def main():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

    print('getting list')
    file_list = drive.ListFile({'q': "trashed = true"}).GetList()
    print('have the list')
    for file in file_list:
        title = file['title']
        id = file['id']
        print(f'title: {title}, id: {id}')
        file.UnTrash()

if __name__ == "__main__":
    main()
