
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到script部分
old_script_end = '''    &lt;script&gt;
        function unlockWebsite() {
            const splash = document.getElementById('splash-screen');
            splash.style.opacity = '0'; 
            
            setTimeout(() =&gt; {
                splash.style.display = 'none'; 
                // 开始显示文字动画
                showTextAnimations();
            }, 2000); 
        }
        
        function showTextAnimations() {
            setTimeout(() =&gt; {
                document.querySelector('.m1-part1').classList.add('show');
            }, 0);
            setTimeout(() =&gt; {
                document.querySelector('.m1-part2').classList.add('show');
            }, 1000);
            setTimeout(() =&gt; {
                document.querySelector('.m1-part3').classList.add('show');
            }, 2000);
        }
    &lt;/script&gt;'''

new_script_end = '''    &lt;script&gt;
        function unlockWebsite() {
            const splash = document.getElementById('splash-screen');
            splash.style.opacity = '0'; 
            
            setTimeout(() =&gt; {
                splash.style.display = 'none'; 
                // 开始显示文字动画
                try {
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
                } catch(e) {
                    console.log(e);
                }
            }, 2000); 
        }
    &lt;/script&gt;'''

if old_script_end in content:
    content = content.replace(old_script_end, new_script_end)
else:
    # 尝试另一种方式
    print('尝试另一种方式...')
    # 直接找到 unlockWebsite 函数并替换
    import re
    pattern = r'function unlockWebsite\(\)[\s\S]*?</script>'
    replacement = '''function unlockWebsite() {
            const splash = document.getElementById('splash-screen');
            splash.style.opacity = '0'; 
            
            setTimeout(() =&gt; {
                splash.style.display = 'none'; 
                // 开始显示文字动画
                try {
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
                } catch(e) {
                    console.log(e);
                }
            }, 2000); 
        }
    &lt;/script&gt;'''
    content = re.sub(pattern, replacement, content)

with open('d:\\桌面\\birthday_site\\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('修复完成！')
