import os
import dlib
import numpy as np  
import cv2     
import time     


def copy_pics(input, output):

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('xxx.dat')


    path = "manual_testing/"
    img = cv2.imread(path+input)


    faces = detector(img, 1)

    print("faces in all:", len(faces), "\n")


    height_max = 0
    width_sum = 0


    for face in faces:


        pos_start = tuple([face.left(), face.top()])
        pos_end = tuple([face.right(), face.bottom()])


        height = face.bottom()-face.top()
        width = face.right()-face.left()

        width_sum += width

        if height > height_max:
            height_max = height
        else:
            height_max = height_max


    print("The size of window:"
        , '\n',"height:", height_max
        , '\n',"width: ", width_sum)


    img_blank = np.zeros((height_max, width_sum, 3), np.uint8)


    blank_start = 0


    for face in faces:

        height = face.bottom()-face.top()
        width = face.right()-face.left()


        for i in range(height):
            for j in range(width):
                    img_blank[i][blank_start+j] = img[face.top()+i][face.left()+j]
        blank_start += width

    cv2.namedWindow("img_faces")#, 2)
    outt = "manual_testing_cropped/"+str(output)
    cv2.imwrite(outt,img_blank)

for im in os.listdir("manual_testing/"):
    print(im)
    try:
        copy_pics(im,im)
    except:
        pass
    