'''
    Test for compare_code in get_color file.
    this tests for comparing the user guess with the secret code using visual inspect
'''
from get_color import compare_code

def test_1bull_1cow():
    ''' test for one bull one cow '''
    
    code = ["red", "blue", "green", "yellow"]
    guess = ["red", "purple", "black", "blue"]
    bulls, cow = compare_code(code, guess)

    if bulls == 1 and cow == 1:
        print("test passed: 1bull 1cow")
        print("expected: bulls: 1 cow: 1")
        print(f"actual: bulls: {bulls} cow: {cow}")
    else:
        print(f"test failed- {bulls}:  {cow}: ")

def test_all_bull():
    ''' test for all bulls '''
    
    code = ["red", "blue", "green", "yellow"]
    guess = ["red", "blue", "green", "yellow"]
    bulls, cow = compare_code(code, guess)

    if bulls == 4 and cow == 0:
        print("test passed: all bulls")
        print("expected: bulls: 4 cow: 0")
        print(f"actual: bulls: {bulls} cow: {cow}")
    else:
        print(f"test failed- {bulls}:  {cow}: ")
    
def test_all_cow():
    ''' test for all cows '''
    
    code = ["red", "blue", "green", "yellow"]
    guess = ["yellow", "red", "blue", "green"]
    bulls, cow = compare_code(code, guess)

    if bulls == 0 and cow == 4:
        print("test passed: all cow")
        print("expected: bulls: 0 cow: 4")
        print(f"actual: bulls: {bulls} cow: {cow}")
    else:
        print(f"test failed- {bulls}:  {cow}: ")

def test_2bull_2cow():
    ''' test for two bull two cow '''
    
    code = ["green", "yellow", "purple", "black"]
    guess = ["green", "yellow", "black", "purple"]
    bulls, cow = compare_code(code, guess)

    if bulls == 2 and cow ==2:
        print("test passed: 2bull 2cow")
        print("expected: bulls: 2 cow: 2")
        print(f"actual: bulls: {bulls} cow: {cow}")
    else:
        print("test failed")
        print("expected: bulls: 2 cow: 2")
        print(f"actual bulls: {bulls} cow: {cow}")

def main():
    test_1bull_1cow()
    test_all_bull()
    test_all_cow()
    test_2bull_2cow()

if __name__ == "__main__":
    main()
