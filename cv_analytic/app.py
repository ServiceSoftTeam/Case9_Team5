from ai.cv_ai import cv_detection
# from visual_odometry.vo import vo_video
import requests


def main(object):
    # image = vo_video(object)
    analytic = cv_detection(object)
    print(analytic)
    r = requests.post(
        "http://87.244.7.150:8000/api/samolet/get_unchaked/", data=analytic)
    print(r.status_code)


if __name__ == '__main__':
    print(main('static/7.mp4'))
