
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 删除第2108行（索引是2107）
del lines[2107]

with open('d:\\桌面\\birthday_site\\index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('删除完成！')
