def check_boss_baby_revenge(s):
    # Find first positions of 'S' and 'R' (returns -1 if not found)
    first_s = s.find('S')
    first_r = s.find('R')
    print(first_s, first_r)

    # Check if 'R' appears before 'S' or if 'R' exists but 'S' doesn't
    if first_r != -1 and (first_s == -1 or first_r < first_s):
        return "Bad boy"
    
    # Count total 'S' and 'R'
    total_s = s.count('S')
    total_r = s.count('R')
    print(total_s, total_r)
    
    # Check if 'R' count is less than 'S' count
    if total_r < total_s:
        return "Bad boy"
    
    return "Good boy"


val = input("Enter your value: ")
print(check_boss_baby_revenge(val))