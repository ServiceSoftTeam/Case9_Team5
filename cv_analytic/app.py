from visual_odometry.vo import vo_video
import requests
from time import sleep

def main():
    while True:
        r = requests.get("http://87.244.7.150:8000/api/samolet/get_unchaked/")
        data = r.json()
        if data is not None:
            if data['analysis'] is None:
                analytic = vo_video(object)
                print(analytic)
                r = requests.put(
                    f"http://87.244.7.150:8000/api/samolet/checks/{data['id']}", data=analytic)
                print(r.status_code)
            sleep(5)


if __name__ == '__main__':
    main()
