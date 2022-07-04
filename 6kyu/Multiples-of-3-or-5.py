def solution(number):
    output = 0
    for i in range(number):
        if (i % 3 == 0) or (i % 5 == 0):
            output += i
            continue
        elif (i % 5 == 0):
            output += i
            continue
        else:
            continue
            
    return (output)
        
        
        
solution(1000)