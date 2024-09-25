from pynput import mouse
from PIL import ImageGrab, Image, ImageCms
import matplotlib.pyplot as plt
import cv2
import pyautogui
import colorAnalizer
import numpy as np
import popUp

# わざわざ main 関数を定義してその中に処理を書く
def main():
    # マウスリスナーを作成
    listener = mouse.Listener(on_click=on_click)

    # マウスリスナーを開始（非同期で実行される）
    listener.start()

    # プログラムを終了するためにキー入力待ち（任意）
    input("プログラムを終了するには何かキーを押してください...")

# マウスのクリックイベントを処理する関数
def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        # スクリーン全体のスクリーンショットを取得
        screenshot = ImageGrab.grab()
        print("size = ", screenshot.size)
        print("(x, y) = ", x, y)
        
        # 指定した位置のピクセルの色を取得
        color = screenshot.getpixel((x*2, y*2))
        
        nearest_color_name = colorAnalizer.find_nearest_color(np.array(color[:3], np.uint8))
        
        
        print(f"左クリックされた位置の色: {nearest_color_name}")
        
        print(f"左クリックされた位置の色: {color}")
        
        popUp.show_color_popup(x, y, color, nearest_color_name)
        
        # スクリーンショットを表示
        # screenshot.show()



# try:
#     while True:
#         x, y = pyautogui.position()
#         rgb = pyautogui.screenshot().getpixel((x*2, y*2))
#         text = 'X:{} Y:{} RGB:({}, {}, {})'.format(
#             str(x).rjust(4), 
#             str(y).rjust(4),
#             str(rgb[0]).rjust(3),
#             str(rgb[1]).rjust(3),
#             str(rgb[2]).rjust(3))
#         print(text, end='')
#         print('\b' * len(text), end='', flush=True)

# except KeyboardInterrupt:
#     print('\n終了。')

if __name__ == "__main__":
    main()