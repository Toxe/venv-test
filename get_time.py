import requests


if __name__ == "__main__":
    r = requests.get("http://worldtimeapi.org/api/timezone/Europe/Berlin", timeout=10)
    if r.status_code == 200:
        data = r.json()
        print(data["datetime"])
