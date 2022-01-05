import cv2
import mediapipe as mp
import time

class poseDetector():
    def __init__(self, mode, upBody =False, smooth =True, detectionCon = 0.5, trackCon=0.5):
        self.mode = mode
        self.upBody =upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

        def findPose(self, img, draw=True):

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.results = self.pose.process(imgRGB)
            # print(results.pose_landmarks)

            if self.results.pose_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        # for id, lm in enumerate(results.pose_landmarks.landmark):
        #     h, w, c = img.shape
        #     print(id,lm)
        #     cx, cy = int(lm.x*w), int(lm.y*h)
        #     cv2.circle(img, (cx, cy), 10, (255, 0,0), cv2.FILLED)


def main():
    cap = cv2.VideoCapture('PoseVideos/1.mp4')
    pTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        detector.findPose
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 0, 0), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()