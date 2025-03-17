import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$½%&+/*-_?"

all_chars = lower_case + upper_case + numbers + symbols
length_for_pass = 8

# Ensure at least one character from each category
password = (
    random.choice(lower_case) +
    random.choice(upper_case) +
    random.choice(numbers) +
    random.choice(symbols) +
    "".join(random.sample(all_chars, length_for_pass - 4))
)

# Shuffle the password to increase randomness
password = "".join(random.sample(password, len(password)))

print("Your generated password is:", password)
