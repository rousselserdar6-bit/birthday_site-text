
# 读取文件
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义宜昌的照片列表
yichang_photos = [
    '宜昌/3503c13d282d56b7ce5e794a452c2473.jpg',
    '宜昌/4080fbd1ddaa60fa5af4455b944afbff.jpg', 
    '宜昌/4862981e998037456a271234c7102e46.jpg',
    '宜昌/7c50bf109555fbeafd4dac9cff55d4d1.jpg',
    '宜昌/862f6fed587d6ef91b094d2441339b0a.jpg',
    '宜昌/a02d22836fa964bf49d927144260eda6.jpg',
    '宜昌/a3942e91112932e2ae2323ac4296335a.jpg',
    '宜昌/ded8d9e5fb6fe0c9cd393ddc3a59aa94.jpg'
]

# 转换为字符串格式
photo_str = "['" + "', '".join(yichang_photos) + "']"

# 替换旅行日记中的宜昌卡片（使用实际的&amp;）
old_photo_str = "['https://images.unsplash.com/photo-1505993597083-3bd19fd75e77?q=80&w=500', 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=500']"
content = content.replace(old_photo_str, photo_str)

# 替换卡片背景图
old_bg = "url('https://images.unsplash.com/photo-1505993597083-3bd19fd75e77?q=80&w=500')"
new_bg = f"url('{yichang_photos[0]}')"

# 只替换宜昌卡片的背景图（第一个出现的背景图是宜昌的）
# 先找到宜昌卡片的位置，然后替换
index = content.find('宜昌 · 三峡')
if index != -1:
    # 在宜昌卡片之前的背景图就是我们要替换的
    part1 = content[:index]
    part2 = content[index:]
    # 在part1中找到最后一个背景图
    last_bg_pos = part1.rfind(old_bg)
    if last_bg_pos != -1:
        content = part1[:last_bg_pos] + new_bg + part1[last_bg_pos + len(old_bg):] + part2

# 写回文件
with open('d:\\桌面\\birthday_site\\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("宜昌照片更新成功！")
