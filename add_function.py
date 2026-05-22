
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '''        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;'''

replace_with = '''        }

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
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;'''

content = content.replace(target, replace_with)

with open('d:\\桌面\\birthday_site\\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('添加成功！')
