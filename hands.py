import cv2
import mediapipe as mp
mpdrawing=mp.solutions.drawing_utils
mphands=mp.solutions.hands
width,heght=1280,720
video=cv2.VideoCapture(0)
video.set(3,width)
video.set(4,heght)
with mphands.Hands(min_tracking_confidence=0.5,max_num_hands=2,min_detection_confidence=0.5) as hands:
    while True:
        success,img=video.read()
        results=hands.process(img)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                mpdrawing.draw_landmarks(img,landmark_list=landmarks,connections=mphands.HAND_CONNECTIONS)
        if results.multi_hand_landmarks:
            myhannd=results.multi_hand_landmarks[handNo]

        cv2.imshow("Img",cv2.flip(img,1))
        if not success:
            break
        if cv2.waitKey(10)==ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()