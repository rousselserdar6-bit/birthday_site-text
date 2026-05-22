
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找到script部分的起始
# 我们要从第2117行到结束替换
for i in range(len(lines)):
    if lines[i].strip() == '<script>' and i &gt; 2100:
        break

# i 是 2116（索引）
new_script = '''    &lt;script&gt;
        function unlockWebsite() {
            const splash = document.getElementById('splash-screen');
            splash.style.opacity = '0'; 
            
            setTimeout(() =&gt; {
                splash.style.display = 'none'; 
                // 开始显示文字动画
                setTimeout(() =&gt; {
                    const part1 = document.querySelector('.m1-part1');
                    if (part1) part1.classList.add('show');
                }, 0);
                setTimeout(() =&gt; {
                    const part2 = document.querySelector('.m1-part2');
                    if (part2) part2.classList.add('show');
                }, 1000);
                setTimeout(() =&gt; {
                    const part3 = document.querySelector('.m1-part3');
                    if (part3) part3.classList.add('show');
                }, 2000);
            }, 2000); 
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;'''

# 删除从第2116行到结束，然后添加新script
lines = lines[:2116]
lines.append(new_script)

with open('d:\\桌面\\birthday_site\\index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('修复完成！')
