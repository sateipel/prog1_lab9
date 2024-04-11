def main():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(password):
    encoded_password = ''
    for i in range(len(password)):
        index_val=int(password[i])
        index_val+=3
        encoded_password+=str(index_val)
    return encoded_password
def decoder(s):
    new = ""
    for letter in s:
        num = int(letter)
        if num == 2:
            new += "9"
        elif num == 1:
            new += "8"
        elif num == 0:
            new+= "7"
        else:
            num -= 3
            new += str(num)
    return new

if __name__ == "__main__":
    password = ''
    while True:
        choice=int(input("Please enter an option: "))
        if choice==1:
            new_password = input("Please enter your password: ")
            encode(new_password)
            print("Your password has been encoded and stored!")
            continue
        #if choice==2:
        if choice==3:
            break