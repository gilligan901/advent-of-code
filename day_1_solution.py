import day_1_input

number_dict = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

def findfirstdigit(line):
    new_line =''
    for character in line:
        if character.isdigit():
            return character
        
        new_line += character
        for key in number_dict:
            if new_line.find(key) != -1:
                return str(number_dict[key])

def findlastdigit(line):
    new_line =''
    for character in line[::-1]:
        if character.isdigit():
            return character
         
        new_line = character + new_line
        for key in number_dict:
            if new_line.find(key) != -1:
                return str(number_dict[key])

total = 0

for line in day_1_input.real_data_2.splitlines():
    digits = findfirstdigit(line)+findlastdigit(line)
    print(digits)
    total += int(digits)

print(total)