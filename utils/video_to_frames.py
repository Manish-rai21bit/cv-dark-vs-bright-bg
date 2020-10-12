# https://theailearner.com/2018/10/15/extracting-and-saving-video-frames-using-opencv-python/
import cv2  # still used to save images out
import glob
import os


def get_video_to_frame(video_path, frames_dir, every):
    # Opens the Video file
    cap = cv2.VideoCapture(video_path)
    i = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        if i%every == 0:
            cv2.imwrite(os.path.join(frames_dir,str(i)+'.jpg'), frame)
        i += 1

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # test it
    for v in glob.glob('/Users/rai00007/Desktop/computer_vision/data/videos/*'):
        print(v)
        get_video_to_frame(video_path=v, frames_dir='/Users/rai00007/Desktop/computer_vision/output/v2f/', every=20)
