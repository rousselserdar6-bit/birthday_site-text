
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找到script标签结束的位置
# 我们需要找到 lines.index('    </script>\n') 或者类似的

# 查找关键行
for i in range(len(lines)):
    if '</script>' in lines[i] and 'unlockWebsite' in lines[i-5]:
        break

# i 应该是 2128（索引）
# 在 i 前面插入新函数
insert_index = i
new_lines = [
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
    '        \n'
]

for line in reversed(new_lines):
    lines.insert(insert_index, line)

with open('d:\\桌面\\birthday_site\\index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('完成！')
