import math
summ = 0
tot_sum=0
ttt = 0

def prime(i):
    if i == 1 :
        return True
    if i == 2 or i == 0:
        return False
    sqrt_i = int(math.sqrt(i))+1
    for j in range(2,sqrt_i):
        if i%j == 0:
            return True
    return False

#test=[[1],[8,4],[2,6,9],[8,5,9,3]]

test=[
[215],
[193,124],
[117,237,442],
[218 ,935 ,347 ,235],
[320 ,804 ,522 ,417 ,345],
[229 ,601 ,723 ,835, 133, 124],
[248 ,202 ,277 ,433 ,207 ,263 ,257],
[359 ,464 ,504 ,528, 516, 716, 871 ,182],
[461 ,441 ,426, 656, 863, 560, 380 ,171 ,923],
[381, 348 ,573, 533, 447, 632, 387, 176, 975, 449],
[223 ,711 ,445 ,645 ,245 ,543 ,931 ,532 ,937 ,541 ,444],
[330 ,131, 333 ,928 ,377 ,733 ,17, 778 ,839 ,168 ,197, 197],
[131 ,171 ,522 ,137, 217 ,224, 291 ,413 ,528, 520, 227, 229 ,928],
[223 ,626 ,34, 683, 839, 53, 627, 310, 713, 999, 629, 817, 410, 121],
[924, 622, 911, 233, 325, 139, 721, 218, 253, 223, 107, 233, 230, 124, 233]]

def solve(i1,i2):
    global summ
    global tot_sum
    if not prime(test[int(i1)][int(i2)]):
        return False
    
    summ += test[int(i1)][int(i2)]
    #print("Added",test[int(i1)][int(i2)])
    
    cont = True
    if i1+1<len(test):
        
        cont = cont & solve(int(i1+1),int(i2))
        if i2+1 < len(test[int(i1+1)]):
            cont = cont | solve(int(i1+1),int(i2+1))
    else:
        if summ > tot_sum:
            tot_sum = summ
            cont = True
    
    summ-=test[int(i1)][int(i2)]
    #print("Deleted",test[int(i1)][int(i2)])
    return cont

    

solve(0,0)
print('Total:',tot_sum)
