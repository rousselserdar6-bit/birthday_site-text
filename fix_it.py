
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找到第2127行（索引是2126） - 是 '        }\n'
# 然后在这行之后添加新函数

# 让我们查看那附近的内容
for i in range(2120, 2135):
    print(f"{i}: {repr(lines[i])}")

# 现在修改
insert_pos = 2127
new_function_lines = [
    '        \n',
    '        function showTextAnimations() {\n',
    '            setTimeout(() =&gt; {\n',
    "                document.querySelector('.m1-part1').classList.add('show');\n",
    '            }, 0);\n',
    '            setTimeout(() =&gt; {\n',
    "                document.querySelector('.m1-part2').classList.add('show');\n",
    '            }, 1000);\n',
    '            setTimeout(() =&gt; {\n',
    "                document.querySelector('.m1-part3').classList.add('show');\n",
    '            }, 2000);\n',
    '        }\n',
]

for line in reversed(new_function_lines):
    lines.insert(insert_pos, line)

with open('d:\\桌面\\birthday_site\\index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('成功！')
