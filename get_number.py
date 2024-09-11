import  easyocr

images_path = "./car_plates/scaned_img_2.jpg"

reader = easyocr.Reader(["en"], gpu=True)

result = reader.readtext(images_path)

car_num = result[-1][-2]
print(result)
print("car_num", car_num)