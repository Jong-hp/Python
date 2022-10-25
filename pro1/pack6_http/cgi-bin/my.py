# 사용자가 전송한 정보를 수신 후 ...

import cgi

form = cgi.FieldStorage()
irum = form['name'].value
nai = form['age'].value
    
print('Content-Type:text/html;charset=utf-8\n')
print('''
<html>
<body>
이름은 {0}
<br>
나이는 {1}
</body>
</html>
'''.format(irum, nai))