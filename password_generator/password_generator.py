import string
import secrets

# Build character set
def build_dict(low, up, dig, spec):
    char_set = ""
    if low:
        char_set += string.ascii_lowercase
    if up:
        char_set += string.ascii_uppercase
    if dig:
        char_set += string.digits
    if spec:
        char_set += string.punctuation
    return char_set
           
# Generate password  
def password_generator(length, lower, upper, digits, special):
    char_set = build_dict(lower, upper, digits, special) 
    
    password = ""
    for num in range(length):
        letter = secrets.choice(char_set)
        password += letter
    return password

def main():
    result = password_generator(10, True, True, True, True)
    print(result)
    
main()
