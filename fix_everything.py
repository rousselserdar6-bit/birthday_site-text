
with open('d:\\桌面\\birthday_site\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 第一步：修复HTML转义的问题
# 把 &lt;script&gt; 替换回 <script>
content = content.replace('&lt;script&gt;', '<script>')
content = content.replace('&lt;/script&gt;', '</script>')
content = content.replace('&lt;/body&gt;', '</body>')
content = content.replace('&lt;/html&gt;', '</html>')
content = content.replace('&amp;', '&')

with open('d:\\桌面\\birthday_site\\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('HTML转义修复完成！')
