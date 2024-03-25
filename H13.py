def kill(input_str):
    groups=input_str.split('$')
    min_lengh=float('inf')
    for group in groups:
        subgroups=group.split('@')
        lengths=[len(subgroup) for subgroup in subgroups]
        min_lengh=min(min_lengh, min(lengths))
    return min_lengh
input_str=input("Enter a sequence")
res=kill(input_str)
print(res)