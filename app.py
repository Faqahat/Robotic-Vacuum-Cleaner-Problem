import numpy as np
s = '445621207591863034'
s = '445621997591863034'
s = np.array(list(s), dtype=np.uint8)
x = s[2:].reshape(s[0],-1)
size = s[0]
highest = 0
cords = {}
for i in range(0, len(s)):
    if i > 0:
        for j in range(0, len(s)):
            sum = 0
            if i + 1  <  size and i  <  size and  j  <  size and j + 1  <  size:
                sum = x[i][j]  + x[i+1][j] + x[i][j+1] + x[i+1][j+1]
                if sum > highest:
                    highest = sum
                    cords = {
                        "a" : i,
                        "b" : i+1,
                        "c" : j,
                        "d" : j+1
                    }
print "(", cords["b"] , "," , cords["c"], ")", "(", cords["d"] , "," , cords["b"] , ") ","(", cords["d"] , "," , cords["a"] , ")" ,"(", cords["c"] , "," , cords["a"] , ")" , highest

 
                



