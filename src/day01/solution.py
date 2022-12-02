def part1(data):
     data.append("")
     cal = 0
     cal_list = []
     for n in data:        
         if n != "":
             cal += int(n)
         elif n == "":
             cal_list.append(cal)
             cal = 0
     cal_list.sort(reverse=True)       
    print(cal_list [0])
    
     return cal_list
 
################################################################################
def part2(data):
    data.append("")
    cal = 0
    top_cal = 0
    cal_list = []
    for n in data:        
        if n != "":
            cal += int(n)
        elif n == "":
            cal_list.append(cal)
            cal = 0
    cal_list.sort(reverse=True)       
    top_cal = sum(cal_list [0:3])
    # print(top_cal)

    return top_cal



data = open("src/day01/input.txt", "r").readlines()
# data = open("src/day01/example.txt", "r").readlines()

data = [line.strip("\n") for line in data]

print(part1(data))
print(part2(data))
