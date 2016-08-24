def right_justify(str):
    length = len(str);
    new_str = ' ' * (70 - length) + str
    print new_str


right_justify('test');