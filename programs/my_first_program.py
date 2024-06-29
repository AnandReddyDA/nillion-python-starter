from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform bitwise AND operation on my_int1 and my_int2
    result = my_int1 & my_int2

    return [Output(result, "bitwise_and_output", party1)]
