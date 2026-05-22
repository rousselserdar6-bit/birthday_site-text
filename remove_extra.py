
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找到第2138行是 '        }\n'
# 然后删除从2139到2150行
# 保留到2138行，然后加上最后的</script></body></html>

new_lines = lines[:2139]
new_lines.extend([
    '    &lt;/script&gt;\n',
    '&lt;/body&gt;\n',
    '&lt;/html&gt;'
])

with open('d:\\桌面\\birthday_site\\index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('成功！')
