def MyCandles(specs):
    candle = specs[0]
    days = specs[1]
    
    numCandles = days + ((days * (days + 1))/2)
    print('{0} {1}'.format(candle, int(numCandles)))

num = int(input())
for i in range(num):
    _specs = [int(j) for j in input().split()]
    MyCandles(_specs)
