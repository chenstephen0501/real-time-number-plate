# 車牌辨識 (Real-Time Number Plate)

![演示影片](/public/video/number_plate.gif)
[專案演示影片完整連結](https://youtu.be/gNv1vAh3FKM)

## 介紹
「車牌辨識」專案是一個即時車牌辨識工具。此專案利用 easyocr 進行光學字符識別，並使用 opencv-python 處理影像和顯示結果。車牌檢測使用了 OpenCV 的預訓練模型 haarcascade_russian_plate_number.xml。

## 功能
- 即時檢測車牌號碼，將檢測到的車牌圖像儲存，最後顥示車牌辨的結果
- 另外支援按鍵操作：s 保存圖像，e 隱藏提示，q 退出程序

## 系統需求

### Python 環境與套件

- python 3.12
- easyocr 1.7.1
- opencv-python 4.10.0.84

## 安裝與設定

### 1. 克隆專案，將專案克隆至本地
```bash
$ git clone git@github.com:chenstephen0501/todo_list_backend.git
$ cd todo_list_backend
```

### 2. 虛擬環境初始化

```bash
$ pip install poetry
```

### 3. 進入虛擬環境
```bash
$ poetry shell
$ poetry install
```

### 4. 啓動 usb 攝像頭對車牌進行辨視
```bash
$ python car_number_plate.py
```

### 5. 將車牌辨後的圖檔進行解析並輸出結果
```bash
$ python get_number.py
```
