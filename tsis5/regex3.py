import re

string1 = "This is_a siuuu_text with_aibo sequences_of_lowercase_letters_joined_with_underscores."


sequence = re.findall(r'\b[a-z]+(?:_[a-z]+)+\b', string1)
    
print("Нашлось:")
for x in sequence:
    print(x)
