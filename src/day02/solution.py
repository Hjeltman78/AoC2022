# def part1(data):
#     total = 0
#     A = rock = X = 1
#     B = paper = Y = 2
#     C = sciss = Z = 3
#     loss = 0
#     draw = 3
#     win = 6
    
#     # signs = ["rock", "paper", "sciss"]
            
#     # op_sign = {"rock": A, "paper": B, "sciss": C}
#     # my_sign = {"rock": X, "paper": Y, "sciss": Z}
        
    
#     for row in data:
#         if "A X" in row:
#             total += X + draw
#         if "B X" in row:
#             total += X + loss
#         if "C X" in row:
#             total += X + win
#         if "A Y" in row:
#             total += Y + win
#         if "B Y" in row:
#             total += Y + draw
#         if "C Y" in row:
#             total += Y + loss
#         if "A Z" in row:
#             total += Z + loss
#         if "B Z" in row:
#             total += Z + win
#         if "C Z" in row:
#             total += Z + draw
#     print(total)        
                
        
        
        
   
# # rock = 1, papper = 2, sciss = 3
# # los = 0, draw = 3, win = 6
# # 
#     return data




################################################################################
def part2(data):
    total_2 = 0
    rock = A = 1 
    pap = B = 2
    scis = C = 3
    X = loss = 0
    Y = draw = 3
    Z = win = 6
    
   
    
    for row in data:
        if "A X" in row:
            total_2 += C + loss
        if "B X" in row:
            total_2 += A + loss
        if "C X" in row:
            total_2 += B + loss
        if "A Y" in row:
            total_2 += A + draw
        if "B Y" in row:
            total_2 += B + draw
        if "C Y" in row:
            total_2 += C + draw
        if "A Z" in row:
            total_2 += B + win
        if "B Z" in row:
            total_2 += C + win
        if "C Z" in row:
            total_2 += A + win
    print(total_2)        
                
    
    return data


data = open("src/day02/input.txt", "r").readlines()
# data = open("src/day02/example.txt", "r").readlines()

data = [line.strip("\n") for line in data]

# print(part1(data))
print(part2(data))
