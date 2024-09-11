import cv2
# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture(1, cv2.CAP_DSHOW)

capture.set(3, 640)
capture.set(4, 480)

min_plate_area = 500
count = 0

while True:
    success, img = capture.read()

    if not success:
        print("Failed to open the camera!")
        break

    car_plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    car_plates = car_plate_cascade.detectMultiScale(img_gray, 1.1, 4)
    for(x, y, w, h) in car_plates:
        plate_area = w * h

        if plate_area > min_plate_area:
            cv2.rectangle(img, (x, y), (x+w, y+h),(0, 255, 0), 2)
            cv2.putText(img, "Car Plate", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_plate_image = img[y: y+h, x: x+w]
            cv2.imshow("Plate Image", img_plate_image)

    cv2.imshow("Opening", img)

    if cv2.waitKey(1) & 0XFF == ord("s"):
        cv2.imwrite("car_plates/scaned_img_" + str(count) + ".jpg", img_plate_image)  
        cv2.rectangle(img, (0, 200), (640, 300), (0, 250, 0), cv2.FILLED)      
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)      
        cv2.imshow("Saved", img)      
        cv2.waitKey(500)      
        count += 1
    elif cv2.waitKey(1) & 0XFF == ord("e"):
        cv2.destroyWindow("Saved")
    elif cv2.waitKey(1) & 0XFF == ord("q"):  
        capture.release()
        cv2.destroyAllWindows()