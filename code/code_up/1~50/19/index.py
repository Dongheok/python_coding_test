# [기초-입출력] 연월일 입력받아 그대로 출력하기

a, b, c = map(int, input().split('.'))


def year_fn(yr):
    if yr >= 1000:
        return "%s" % yr
    elif yr >= 100:
        return "0"+"%s" % yr
    elif yr >= 10:
        return "0"+"0"+"%s" % yr
    elif yr >= 0:
        return "0"+"0"+"0"+"%s" % yr


def date_fn(dt):
    if dt >= 10:
        return "%s" % dt
    else:
        return "0"+"%s" % dt


result = year_fn(a) + '.' + date_fn(b) + '.' + date_fn(c)

print(result)


# y,m,d = map(str,input().split('.'))

# if len(m)<2 : m = "0"+m
# if  len(d)<2: d = "0"+d
# if len(y) == 3: y = "0"+y
# elif len(y) == 2: y = "00"+y
# elif len(y)==1: y = "000"+y

# print("%s.%s.%s"%(y,m,d))
