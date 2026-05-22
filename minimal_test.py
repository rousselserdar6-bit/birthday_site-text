
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找到script起始
for i in range(len(lines)):
    if lines[i] == '    <script>\n' and i > 2100:
        start = i
        break

# 使用最简单的函数
minimal_script = '''    &lt;script&gt;
        function unlockWebsite() {
            const splash = document.getElementById('splash-screen');
            splash.style.opacity = '0'; 
            setTimeout(() =&gt; {
                splash.style.display = 'none'; 
            }, 2000); 
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;'''

new_lines = lines[:start]
new_lines.append(minimal_script)

with open('d:\\桌面\\birthday_site\\index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('修复完成！现在应该可以进入主页了！')
