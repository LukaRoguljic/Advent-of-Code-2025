# DAY 3
def main():
    part_1()
    
def part_1():
    import os
    print("Current working directory:", os.getcwd())
    print(os.listdir("."))
    
    f = open("Day3Input.txt", "r")

    line = f.readline()
    suma = 0
    while line:
        
        clean = line.rstrip("\n")
        clean_arr = list(clean)
        if len(clean_arr) != 0:
            #811111111111119
            left_digit_max = -1
            best_combo_seen = -1
            
            for digit in clean_arr:                
                if left_digit_max != -1:
                    new_combo = left_digit_max * 10 + int(digit) 
                    best_combo_seen = max(best_combo_seen, new_combo)
                    print(new_combo,best_combo_seen)
                    
                left_digit_max = max(left_digit_max, int(digit))
                
            suma = suma + best_combo_seen
            print(left_digit_max)        
        line = f.readline()
    print(suma)         
    f.close()

if __name__ == "__main__":
    main()