from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform arithmetic operations
    sum_result = my_int1 + my_int2
    difference_result = my_int1 - my_int2
    product_result = my_int1 * my_int2
    quotient_result = my_int1 / my_int2  # Assuming the framework handles division by zero internally

    # Output the results
    return [
        Output(sum_result, "sum_output", party1),
        Output(difference_result, "difference_output", party1),
        Output(product_result, "product_output", party1),
        Output(quotient_result, "quotient_output", party1)
    ]

# Example of creating the program
create_program = nada_main()
