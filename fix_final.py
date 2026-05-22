
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 插入位置是第2127行（索引2126）后面
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
