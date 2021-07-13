def dec_to_bin(dec):
    if dec <= 1:
        return dec

    return f"{dec_to_bin(dec//2)}{dec%2}"


print(dec_to_bin(int(input())))
