def xuat(*thamso):
    start = end = step = 0
    if ( len(thamso) == 3):
        start = thamso[0]
        end = thamso[1]
        step = thamso[2]
    elif(len(thamso) == 2):
        start = thamso[0]
        end = thamso[1]
        step = 1
    else:
        start = 0
        end = thamso[0]
        step = 1
    i = start
    while(i < end):
        print(i)
        i = i + step
xuat(2,9)

    
    