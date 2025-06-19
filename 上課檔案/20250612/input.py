print('hi,', input('請輸入姓名'))

import sys
print('請輸入姓名')
for i in sys.stdin:
    print('hi,', i)
    print('請輸入姓名')
