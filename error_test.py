try:
    date = open('missing.txt')
except IOError as err:
    # 给异常对象起名为err
    print('File error:', err)
finally:
    if 'date' in locals():
        date.close()

try:
    with open('its.txt', 'w') as date:
        print("it's a dog.", file=date)
except IOError as err:
    print("file error:" + str(err))
