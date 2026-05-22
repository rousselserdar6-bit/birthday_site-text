with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到第二个script标签开始的位置
script_start = content.find('<script>', content.find('</script>') + 1)
if script_start == -1:
    # 找带空格的
    script_start = content.find('    <script>', content.find('    </script>') + 1)

if script_start >= 0:
    # 找到 </body> 位置
    body_pos = content.find('</body>', script_start)
    if body_pos == -1:
        body_pos = content.find('</html>')
    
    # 新的script标签内容
    new_script_content = '''    <script>
        function unlockWebsite() {
            const splash = document.getElementById('splash-screen');
            splash.style.opacity = '0'; 
            setTimeout(function() {
                splash.style.display = 'none'; 
                setTimeout(function() {
                    const part1 = document.querySelector('.m1-part1');
                    if (part1) part1.classList.add('show');
                }, 0);
                setTimeout(function() {
                    const part2 = document.querySelector('.m1-part2');
                    if (part2) part2.classList.add('show');
                }, 1000);
                setTimeout(function() {
                    const part3 = document.querySelector('.m1-part3');
                    if (part3) part3.classList.add('show');
                }, 2000);
                initClock();
            }, 2000); 
        }

        // 时钟相关变量
        let loveClock, clockWrapper, loveMessage, fixHint;
        let clockActivated = false; 
        let hintTimer = null;
        let digitsContainer;

        function initClock() {
            try {
                // 初始化 DOM 元素
                loveClock = document.getElementById('loveClock');
                clockWrapper = document.getElementById('clockWrapper');
                loveMessage = document.getElementById('loveMessage');
                fixHint = document.getElementById('fixHint');
                digitsContainer = document.getElementById('digits-container');
                
                if (!digitsContainer) {
                    console.log('Clock not ready yet');
                    return;
                }
                
                // 生成数字列
                const leftPositions = [38, 31, 24, 17, 10, 3];
                for (let col = 5; col >= 0; col--) {
                    let colDiv = document.createElement('div');
                    colDiv.className = 'digit-col';
                    colDiv.id = 'col-' + col;
                    colDiv.style.left = leftPositions[col] + 'vmin';
                    
                    for (let num = 0; num <= 9; num++) {
                        let numberDiv = document.createElement('div');
                        numberDiv.className = 'number';
                        numberDiv.id = 'digit-' + col + '-' + num;
                        
                        let upDiv = document.createElement('div');
                        upDiv.className = 'up';
                        upDiv.innerHTML = '<div class="digit">' + num + '</div>';
                        
                        let downDiv = document.createElement('div');
                        downDiv.className = 'down';
                        downDiv.innerHTML = '<div class="digit">' + num + '</div>';
                        
                        numberDiv.appendChild(upDiv);
                        numberDiv.appendChild(downDiv);
                        colDiv.appendChild(numberDiv);
                    }
                    digitsContainer.appendChild(colDiv);
                }
                
                // 时间计算引擎
                const startDate = new Date('2024-09-16T09:00:00').getTime();
                let currentDigits = [-1, -1, -1, -1, -1, -1];
                
                function updateDigit(col, val) {
                    if (currentDigits[col] === val) return;
                    
                    let oldOutgoing = document.querySelectorAll('#col-' + col + ' .outgoing');
                    oldOutgoing.forEach(function(el) {
                        el.className = 'number';
                    });
                    
                    let currentActive = document.querySelector('#col-' + col + ' .is-active');
                    let newActive = document.getElementById('digit-' + col + '-' + val);
                    
                    if (currentActive) currentActive.className = 'number outgoing';
                    if (newActive) newActive.className = 'number is-active';
                    
                    currentDigits[col] = val;
                }
                
                function calculateTime() {
                    let totalHours = 0;
                    if (clockActivated) {
                        const now = new Date().getTime();
                        const diffMs = now - startDate;
                        if (diffMs > 0) {
                            totalHours = Math.floor(diffMs / (1000 * 60 * 60));
                        }
                        if (totalHours > 999999) totalHours = 999999;
                    }
                    
                    let hStr = String(totalHours).padStart(6, '0').split('');
                    for (let i = 0; i < 6; i++) {
                        updateDigit(5 - i, parseInt(hStr[i]));
                    }
                    setTimeout(calculateTime, 60000);
                }
                
                // 时钟交互
                function activateClock() {
                    if (clockActivated) return;
                    clockActivated = true;
                    loveClock.classList.add('activated');
                    calculateTime();
                    loveMessage.classList.add('show');
                    setTimeout(function() {
                        loveMessage.classList.remove('show');
                    }, 3000);
                }
                
                // 初始化
                calculateTime();
                clockWrapper.addEventListener('click', activateClock);
                
            } catch (e) {
                console.error('Clock init error:', e);
            }
        }
    </script>
</body>
</html>'''
    
    new_content = content[:script_start] + new_script_content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Success! Fixed everything!')
