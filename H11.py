def Trinagle_type(trinagle_toy):
    res=[]
    for i in trinagle_toy:
        sides=list(map(int, i.split()))
        sides.sort()
        if len(sides)==3:                
            if sides[0]+sides[1]>sides[2]:
                if sides[0]==sides[1]==sides[2]:
                    res.append("Equi;ateral")
                # print("Equilateral triangle")
                elif sides[0]==sides[1] or sides[1]==sides[2]:
                    res.append("Isoscales")
                # print("Isoscales triangle")
                else:
                    res.append("None of this")
            else:
                res.append("None of this")
    return res
trinagle_toy=['221','333','3 45','113']
print(Trinagle_type(trinagle_toy))
