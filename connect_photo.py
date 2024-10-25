
import os
from PIL import Image

def merge_images_in_folder(split_folder_path, save_path):
    # 确保输出目录存在
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 收集分割后的图片
    images = {}
    for filename in os.listdir(split_folder_path):
        if filename.lower().endswith('.jpg'):
            # 根据命名规则提取出图片的原始名称和位置
            base_name, position = parse_filename(filename)
            if base_name not in images:
                images[base_name] = {}
            images[base_name][position] = os.path.join(split_folder_path, filename)

    # 重新拼接图片
    for base_name, parts in images.items():
        if all(pos in parts for pos in ['top_left', 'top_right', 'bottom_left', 'bottom_right']):
            # 读取分割后的四张图片
            top_left = Image.open(parts['top_left'])
            top_right = Image.open(parts['top_right'])
            bottom_left = Image.open(parts['bottom_left'])
            bottom_right = Image.open(parts['bottom_right'])

            # 获取每张图片的宽和高
            width, height = top_left.size

            # 创建一个新的空白图片来拼接四个部分
            new_img = Image.new('RGB', (width * 2, height * 2))

            # 按照原始位置拼接
            new_img.paste(top_left, (0, 0))
            new_img.paste(top_right, (width, 0))
            new_img.paste(bottom_left, (0, height))
            new_img.paste(bottom_right, (width, height))

            # 保存重新拼接的图片
            merged_filename = os.path.join(save_path, f'{base_name}_merged.jpg')
            new_img.save(merged_filename)
            print(f'图片保存成功: {merged_filename}')
        else:
            print(f"缺少部分分割图像，无法拼接: {base_name}")

def parse_filename(filename):
    # 根据命名规则分离出图片的基础名称和位置
    base, ext = os.path.splitext(filename)
    parts = base.split('_')
    position = '_'.join(parts[-2:])  # 取最后两个部分作为位置
    base_name = '_'.join(parts[:-2])  # 其余部分作为基础名称
    return base_name, position

# 使用函数
merge_images_in_folder(split_folder_path=r'D:\Development\Pycharm\PycharmProjects\yolov5-5.0\runs\detect\exp10',
                       save_path=r'D:\Development\Pycharm\PycharmProjects\yolov5-5.0\pattern_data\IC\IC_merged')
