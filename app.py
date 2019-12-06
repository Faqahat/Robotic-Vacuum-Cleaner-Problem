import numpy as np
f = open("input.txt", "r")
cases = f.readline()
s = f.readline()
s = np.array(list(s), dtype=np.uint8)
x = s[2:].reshape(s[0],-1)
size = s[0]
cords = {
    "sum" : 0
}
for i in range(0, len(s)-2):
    
        for j in range(0, len(s)):
            sum = 0
            if i + 1  <  size and i  <  size and  j  <  size and j + 1  <  size:
                sum = x[i][j]  + x[i+1][j] + x[i][j+1] + x[i+1][j+1]
                if sum > cords["sum"]:
                    highest = sum
                    cords = {
                        "a" : i,
                        "b" : i+1,
                        "c" : j,
                        "d" : j+1,
                        "sum" : sum
                    }
print ("(", cords["c"] , "," , cords["b"], ")", "(", cords["d"] , "," , cords["b"] , ") ","(", cords["d"] , "," , cords["a"] , ")" ,"(", cords["c"] , "," , cords["a"] , ")" , cords["sum"])

 
                



