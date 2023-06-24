import requests
import os

def get_latest_release():
  url = 'https://github.com/GoldFirey124YT/VibOS/releases/latest'
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    return data['tag_name']
  else:
    print('Error getting latest release')
    return None

def download_latest_release():
  latest_release = get_latest_release()
  if latest_release is not None:
    url = f'https://github.com/GoldFirey124YT/VibOS/releases/download/{latest_release}/VibOS.zip'
    filename = 'VibOS.zip'
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
      for chunk in response.iter_content(chunk_size=1024):
        f.write(chunk)
  else:
    print('No latest release found')

if __name__ == '__main__':
  download_latest_release()
