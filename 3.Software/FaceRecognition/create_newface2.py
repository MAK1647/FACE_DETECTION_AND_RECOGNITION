import cv2
import shutil
capture_image = cv2.VideoCapture(0)

print("Moi nhap ten cua ban: ")
name = input()
while os.path.exists('C:/Users/nguye/PycharmProjects/BTL/simple_facenet/your_face/' + str(name)):
    print("Da co thu muc cung ten ton tai truoc do, ban muon tiep tuc voi thu muc cu (t) hay nhap lai ten khac (l)")
    s = input()
    while (s != 't') and (s != 'l'):
        print("Da co thu muc cung ten ton tai truoc do, ban muon tiep tuc voi thu muc cu (t) hay nhap lai ten khac (l)")
        s = input()
    if s == 't':
        break
    else:
        print("Moi nhap ten cua ban: ")
        name = input()

print("Chon che do chup tu dong (a) hay thu cong (m)")
mode_capture = input()
while (mode_capture != 'a') and (mode_capture != 'm'):
    print("Chon che do chup tu dong (a) hay thu cong (m)")
    mode_capture = input()

print("Chon che do luu hinh anh: ghi de (w)/ ghi tiep tuc (c)/ xoa va luu hinh anh (d)")
mode_save = input()
while (mode_save != 'w') and (mode_save != 'c') and (mode_save != 'd'):
    print("Chon che do luu hinh anh: ghi de (w)/ ghi tiep tuc (c)/ xoa va luu hinh anh (d)")
    mode_save = input()

import os
os.makedirs('C:/Users/nguye/PycharmProjects/BTL/simple_facenet/your_face/'+str(name), exist_ok=True)
path = 'C:/Users/nguye/PycharmProjects/BTL/simple_facenet/your_face/'+ str(name)
i=1
j=0

if mode_save == 'd':
    shutil.rmtree(path)
    os.makedirs('C:/Users/nguye/PycharmProjects/BTL/simple_facenet/your_face/' + str(name), exist_ok=True)
    path = 'C:/Users/nguye/PycharmProjects/BTL/simple_facenet/your_face/' + str(name)
elif mode_save == 'c':
    while os.path.exists(path + '/' + str(name) + '_'+ str(i) + '.jpg'):
        i += 1

if mode_capture == 'm':
    while capture_image.isOpened():
        ret, frame = capture_image.read()
        cv2.imshow('capture_image', frame)
        if cv2.waitKey(40) == ord('c'):
                cv2.imwrite(os.path.join(path, str(name) + '_' + str(i) + '.jpg'), frame)
                i += 1
        if cv2.waitKey(40) == ord('q'):
            break
elif mode_capture == 'a':
    while capture_image.isOpened():
        ret, frame = capture_image.read()
        cv2.imshow('capture_image', frame)
        j += 1
        if j%10 == 0:
            cv2.imwrite(os.path.join(path, str(name) + '_' + str(i) + '.jpg'), frame)
            if i == 100:
                break
            i += 1
        if cv2.waitKey(40) == ord('q'):
            break

cv2.destroyAllWindows()
