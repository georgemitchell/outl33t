def convert_to_br(user_str):
    for x in user_str:
        print ((ord(x)) * '+' ) +  '.' + ((ord(x)) * '-')

if __name__ == "__main__":
    user_string = raw_input("Enter string for brain fuck generator: ")
    convert_to_br(user_string)
