import numpy as np
from skimage import color

def main():
    RGB1 = np.array([136, 154, 99],np.uint8)
    print(find_nearest_color(RGB1)) # 緑

"""
日本人が認識しやすい色名を基にした色の辞書（RGB値）
"""
css_colors = {
    "赤": np.array([255, 0, 0], np.uint8),
    "青": np.array([0, 0, 255], np.uint8),
    "緑": np.array([0, 128, 0], np.uint8),
    "黄色": np.array([255, 255, 0], np.uint8),
    "黒": np.array([0, 0, 0], np.uint8),
    "白": np.array([255, 255, 255], np.uint8),
    "オレンジ": np.array([255, 165, 0], np.uint8),
    "青紫": np.array([75, 0, 130], np.uint8),
    "赤紫": np.array([128, 0, 128], np.uint8),
    "ピンク": np.array([240, 145, 153], np.uint8),
    "茶色": np.array([150, 80, 66], np.uint8),
    "灰色": np.array([125, 125, 125], np.uint8),
    "水色": np.array([169, 206, 236], np.uint8),
    "紺色": np.array([34, 58, 112], np.uint8),
    "肌色": np.array([244, 190, 155], np.uint8),
}



"""
RGBからLab色空間に変換する関数
"""
def skimage_rgb2lab(rgb):
    return color.rgb2lab(rgb.reshape(1,1,3))


"""
CIEdE2000色差を計算して最も近い色名を返す関数
"""
def find_nearest_color(input_color):
    input_lab = skimage_rgb2lab(input_color)
    nearest_color_name = None
    min_distance = float('inf')
    
    for color_name, color_value in css_colors.items():
        color_lab = skimage_rgb2lab(color_value)
        distance = color.deltaE_ciede2000(input_lab, color_lab)
        if distance < min_distance:
            min_distance = distance
            nearest_color_name = color_name
    
    return nearest_color_name



if __name__ == "__main__":
    main()