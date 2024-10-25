import os
from PIL import Image

def split_images_in_folder(floder_path, save_path):
    # 确保输出目录存在
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # 遍历文件夹图片
    for filename in os.listdir(floder_path):
        if filename.lower().endswith('.jpg'):
            # 构建完整的文件目录
            file_path = os.path.join(floder_path, filename)
            # 切割图片并保存
            split_image(file_path, save_path, filename)

def split_image(file_path, save_path, filename):
    # 打开图片
    with Image.open(file_path) as img:
        print(file_path)
        # 获取图片尺寸
        width, height = img.size

        # 计算分割后的图片尺寸
        new_width = width // 2
        new_height = height // 2

        # 切割图片
        top_left = img.crop((0, 0, new_width, new_height))
        top_right = img.crop((new_width, 0, width, new_height))
        bottom_left = img.crop((0, new_height, new_width, height))
        bottom_right = img.crop((new_width, new_height, width, height))

        # 构建输出文件名
        base, ext = os.path.splitext(filename)
        top_left_filename = f'{save_path}/{base}_top_left{ext}'
        top_right_filename = f'{save_path}/{base}_top_right{ext}'
        bottom_left_filename = f'{save_path}/{base}_bottom_left{ext}'
        bottom_right_filename = f'{save_path}/{base}_bottom_right{ext}'
        # 保存图片
        top_left.save(top_left_filename)
        top_right.save(top_right_filename)
        bottom_left.save(bottom_left_filename)
        bottom_right.save(bottom_right_filename)


# 使用函数
split_images_in_folder(floder_path='D:\Development\Pycharm\PycharmProjects\yolov5-5.0\断裂模式数据\PCB_whole',
                       save_path='D:\Development\Pycharm\PycharmProjects\yolov5-5.0\断裂模式数据\PCB_split')