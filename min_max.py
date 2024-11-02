def minimo_maximo(min,max):
    num_min_max=0
    while num_min_max<min or num_min_max>max:
        print(str('number must be between ')+str(min)+str(" - ")+str(max))
        num_min_max=int(input())
    return num_min_max