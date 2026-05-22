
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到位置并添加函数
# 我们要在第2127行的 } 后面添加函数

# 找到那部分
search_str = '''            setTimeout(() =&gt; {
                splash.style.display = 'none'; 
                // 开始显示文字动画
                showTextAnimations();
            }, 2000); 
        }
    &lt;/script&gt;'''

replace_str = '''            setTimeout(() =&gt; {
                splash.style.display = 'none'; 
                // 开始显示文字动画
                showTextAnimations();
            }, 2000); 
        }

        function showTextAnimations() {
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
    &lt;/script&gt;'''

content = content.replace(search_str, replace_str)

with open('d:\\桌面\\birthday_site\\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('成功！')
