import requests
def get_data_from_api():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response)
    if response.status_code != 200:
        print("failed to call the API")
    else:
        print(response.text)
if __name__ == '__main__':
    get_data_from_api()
