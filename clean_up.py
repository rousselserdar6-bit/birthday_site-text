
# 读取文件
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到旧脚本结束的位置
old_script_start = content.find('&lt;script&gt;', content.find('function unlockWebsite()'))
# 从unlockWebsite函数结束的地方开始查找，找到&lt;/body&gt;之前的所有内容
unlock_end = content.find('&lt;/script&gt;', content.find('function unlockWebsite()')) + len('&lt;/script&gt;')
body_start = content.find('&lt;/body&gt;')

# 删除中间的多余代码
new_content = content[:unlock_end] + '\n' + content[body_start:]

with open('d:\\桌面\\birthday_site\\index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('清理完成！')
