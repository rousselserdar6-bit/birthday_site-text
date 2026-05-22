
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_code = '''    &lt;script&gt;
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

new_code = '''    &lt;script&gt;
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
    &lt;/script&gt;'''

content = content.replace(old_code, new_code)

with open('d:\\桌面\\birthday_site\\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('修复完成！')
