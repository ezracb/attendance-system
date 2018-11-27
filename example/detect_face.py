import cv2
import numpy as np
from detection.FaceDetector import FaceDetector

face_detector = FaceDetector()
image_files = ['./media/train_classfier/ayush/IMG_2945.JPG', './media/train_classfier/ayush/IMG_2946.JPG']
for input_str in image_files:
    # input_str = input('input image file: ')
    # if input_str == 'exit':
    #     break

    img = cv2.imread(input_str)
    boxes, scores = face_detector.detect(img)
    face_boxes = boxes[np.argwhere(scores>0.3)]
    print(face_boxes)
    print(len(face_boxes))
#    for box in face_boxes:
    cv2.rectangle(img, (face_boxes[1], face_boxes[0]), (face_boxes[3], face_boxes[2]), (0, 255, 0), 2)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
