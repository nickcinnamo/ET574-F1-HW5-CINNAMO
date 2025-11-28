from my_math import factorial, mean, fibonacci

def test_factorial():
    print("Testing factorial()")
    tests_passed = True

    try:
        assert factorial(5) == 120
        print("Test 1 (factorial(5)) passed.")
    except AssertionError:
        print("Test 1 (factorial(5)) FAILED.")
        tests_passed = False
        
    try:
        assert factorial(0) == 1
        print("Test 2 (factorial(0)) passed.")
    except AssertionError:
        print("Test 2 (factorial(0)) FAILED.")
        tests_passed = False

    try:
        expected_error = "Error: Input must be a non-negative integer."
        assert factorial(-1) == expected_error
        print("Test 3 (factorial(-1)) passed.")
    except AssertionError:
        print("Test 3 (factorial(-1)) FAILED.")
        tests_passed = False

    try:
        expected_error = "Error: Input must be an integer."
        assert factorial(5.5) == expected_error
        print("Test 4 (factorial(5.5)) passed.")
    except AssertionError:
        print("Test 4 (factorial(5.5)) FAILED.")
        tests_passed = False

    if tests_passed:
        print("All factorial() tests passed successfully!")
    print("-" * 30)


def test_mean():
    print("Testing mean()")
    tests_passed = True

    try:
        assert mean([10, 20, 30]) == 20.0
        print("Test 1 (mean([10, 20, 30])) passed.")
    except AssertionError:
        print("Test 1 (mean([10, 20, 30])) FAILED.")
        tests_passed = False

    try:
        expected_error = "Error: Input list/tuple cannot be empty."
        assert mean([]) == expected_error
        print("Test 2 (mean([])) passed.")
    except AssertionError:
        print("Test 2 (mean([])) FAILED.")
        tests_passed = False

    try:
        result = mean((1.5, 2, 3.5))
        is_close = result > 2.3333 and result < 2.3334
        assert is_close
        print("Test 3 (mean((1.5, 2, 3.5))) passed.")
    except AssertionError:
        print("Test 3 (mean((1.5, 2, 3.5))) FAILED. Result was:", result)
        tests_passed = False

    try:
        expected_error = "Error: Input must be a list or tuple of numbers."
        assert mean(123) == expected_error
        print("Test 4 (mean(123)) passed.")
    except AssertionError:
        print("Test 4 (mean(123)) FAILED.")
        tests_passed = False

    if tests_passed:
        print("All mean() tests passed successfully!")
    print("-" * 30)

def test_fibonacci():
    print("Testing fibonacci()")
    tests_passed = True

    try:
        assert fibonacci(6) == 8
        print("Test 1 (fibonacci(6)) passed.")
    except AssertionError:
        print("Test 1 (fibonacci(6)) FAILED.")
        tests_passed = False

    try:
        assert fibonacci(1) == 1
        print("Test 2 (fibonacci(1)) passed.")
    except AssertionError:
        print("Test 2 (fibonacci(1)) FAILED.")
        tests_passed = False

    try:
        expected_error = "Error: Input must be a positive integer (n >= 1)."
        assert fibonacci(-5) == expected_error
        print("Test 3 (fibonacci(-5)) passed.")
    except AssertionError:
        print("Test 3 (fibonacci(-5)) FAILED.")
        tests_passed = False

    try:
        expected_error = "Error: Input must be an integer."
        assert fibonacci(3.14) == expected_error
        print("Test 4 (fibonacci(3.14)) passed.")
    except AssertionError:
        print("Test 4 (fibonacci(3.14)) FAILED.")
        tests_passed = False

    if tests_passed:
        print("All fibonacci() tests passed successfully!")
    print("-" * 30)


if __name__ == "__main__":
    test_factorial()
    test_mean()
    test_fibonacci()