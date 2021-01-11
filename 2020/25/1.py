def main():
    card_pub_key = 11404017
    door_pub_key = 13768789
    subject = 7

    card_loop_size = decrypt(subject, card_pub_key)
    door_loop_size = decrypt(subject, door_pub_key)

    door_enc_key = transform(door_pub_key, card_loop_size)
    print(door_enc_key)
    card_enc_key = transform(card_pub_key, door_loop_size)
    print(card_enc_key)

def decrypt(subject, key):
    value = 1
    for i in range(1, 50000000):
        value = value * subject
        value = value % 20201227
        if value == key:
            return i

def transform(subject, loop_size):
    value = 1
    for _ in range(loop_size):
        value = value * subject
        value = value % 20201227
    return value

if __name__ == "__main__":
    main()
