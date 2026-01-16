from functions.run_python_file import run_python_file
def main():
    print("Test 1: Run 'main.py' with no arguments")
    print(run_python_file("calculator", "main.py"))

    print("\nTest 2: Run 'main.py' with argument ['3 + 5']")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("\nTest 3: Run 'tests.py'")
    print(run_python_file("calculator", "tests.py"))

    print("\nTest 4: Run '../main.py' (should fail)")
    print(run_python_file("calculator", "../main.py"))

    print("\nTest 5: Run 'nonexistent.py' (should fail)")
    print(run_python_file("calculator", "nonexistent.py"))

    print("\nTest 6: Run 'lorem.txt' (should fail)")
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    main() 