import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AoJocKUpZ5gtWNhC07shKM1tNNfH5_E9mdS9jCXRzSKaukTc4LIRric_8ANyKqa_YB_PMj0wRrC8ES9qctxI1eiKFjAp4brFiTwwqhk9zSkQYPspM96mV79aeB7g6sjAILsLXwg'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")


    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()