
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 在第2123行后面添加一行
# 找到第2123行（索引2122）
# 在这行后面添加代码
# 原来的第2123行是：splash.style.display = 'none'; 
# 然后添加: // 开始显示文字动画
# 然后添加: showTextAnimations();

# 然后在最后一个 script 标签结束前添加新函数

# 替换第2122-2125行
lines[2122] = "                splash.style.display = 'none'; \n"
lines.insert(2123, "                // 开始显示文字动画\n")
lines.insert(2124, "                showTextAnimations();\n")

# 现在添加新函数
new_function = '''        function showTextAnimations() {
            // 第一个文字（生日快乐）立即显示
            setTimeout(() =&gt; {
                document.querySelector('.m1-part1').classList.add('show');
            }, 0);
            
            // 第二个文字1秒后显示
            setTimeout(() =&gt; {
                document.querySelector('.m1-part2').classList.add('show');
            }, 1000);
            
            // 第三个文字2秒后显示
            setTimeout(() =&gt; {
                document.querySelector('.m1-part3').classList.add('show');
            }, 2000);
        }
'''

# 在第2126行后面插入
lines.insert(2127, new_function)

with open('d:\\桌面\\birthday_site\\index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('修改完成！')
