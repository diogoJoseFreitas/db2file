from ftplib import FTP
import paramiko

def ftp_upload(host, username, password, file_path, destination_path):
    try:
        ftp = FTP(host)
        ftp.login(user=username, passwd=password)
        print(f"Connected to FTP server: {host}")

        with open(file_path, 'rb') as file:
            ftp.storbinary(f"STOR {destination_path}", file)
            print(f"File '{file_path}' uploaded to '{destination_path}' on the server.")

        ftp.quit()
        print("FTP connection closed.")
    except Exception as e:
        print(f"FTP upload error: {e}")

def sftp_upload(host, username, password, file_path, destination_path, port=22):
    try:
        transport = paramiko.Transport((host, port))
        transport.connect(username=username, password=password)

        sftp = paramiko.SFTPClient.from_transport(transport)
        print(f"Connected to SFTP server: {host}")

        sftp.put(file_path, destination_path)
        print(f"File '{file_path}' uploaded to '{destination_path}' on the server.")

        sftp.close()
        transport.close()
        print("SFTP connection closed.")
    except Exception as e:
        print(f"SFTP upload error: {e}")


def ftp_download(host, username, password, remote_file_path, local_file_path):
    """
    Connects to an FTP server and downloads a file.

    :param host: FTP server hostname or IP address.
    :param username: FTP username.
    :param password: FTP password.
    :param remote_file_path: Path to the file on the FTP server.
    :param local_file_path: Path to save the downloaded file locally.
    """
    try:
        ftp = FTP(host)
        ftp.login(user=username, passwd=password)
        print(f"Connected to FTP server: {host}")

        with open(local_file_path, 'wb') as file:
            ftp.retrbinary(f"RETR {remote_file_path}", file.write)
            print(f"File '{remote_file_path}' downloaded to '{local_file_path}'.")

        ftp.quit()
        print("FTP connection closed.")
    except Exception as e:
        print(f"FTP download error: {e}")

def sftp_download(host, username, password, remote_file_path, local_file_path, port=22):
    """
    Connects to an SFTP server and downloads a file.

    :param host: SFTP server hostname or IP address.
    :param username: SFTP username.
    :param password: SFTP password.
    :param remote_file_path: Path to the file on the SFTP server.
    :param local_file_path: Path to save the downloaded file locally.
    :param port: Port number for SFTP connection (default is 22).
    """
    try:
        transport = paramiko.Transport((host, port))
        transport.connect(username=username, password=password)

        sftp = paramiko.SFTPClient.from_transport(transport)
        print(f"Connected to SFTP server: {host}")

        sftp.get(remote_file_path, local_file_path)
        print(f"File '{remote_file_path}' downloaded to '{local_file_path}'.")

        sftp.close()
        transport.close()
        print("SFTP connection closed.")
    except Exception as e:
        print(f"SFTP download error: {e}")
   



if __name__ == "__main__":
    # User input to choose protocol
    protocol = input("Enter protocol (ftp/sftp): ").strip().lower()

    # Server details
    host = input("Enter server address: ").strip()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # File paths
    local_file_path = input("Enter local file path: ").strip()
    remote_file_path = input("Enter remote destination path: ").strip()

    if protocol == "ftp":
        ftp_upload(host, username, password, local_file_path, remote_file_path)
    elif protocol == "sftp":
        port = int(input("Enter port (default is 22): ").strip() or 22)
        sftp_upload(host, username, password, local_file_path, remote_file_path, port)
    else:
        print("Invalid protocol. Please choose either 'ftp' or 'sftp'.")

        # User input to choose protocol
    protocol = input("Enter protocol (ftp/sftp): ").strip().lower()

    # Server details
    host = input("Enter server address: ").strip()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # File paths
    remote_file_path = input("Enter remote file path: ").strip()
    local_file_path = input("Enter local file path to save the file: ").strip()

    if protocol == "ftp":
        ftp_download(host, username, password, remote_file_path, local_file_path)
    elif protocol == "sftp":
        port = int(input("Enter port (default is 22): ").strip() or 22)
        sftp_download(host, username, password, remote_file_path, local_file_path, port)
    else:
        print("Invalid protocol. Please choose either 'ftp' or 'sftp'.")
