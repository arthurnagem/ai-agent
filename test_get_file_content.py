from functions.get_file_content import get_file_content

def main():
    print("Test 1: lorem.txt (should truncate at MAX_CHARS)")
    content = get_file_content("calculator", "lorem.txt")
    print(f"Content length: {len(content)}")
    if f"[...File \"lorem.txt\" truncated at" in content:
        print("Truncation message present")
    else:
        print("Truncation message missing")
    print()

    print("Test 2: main.py")
    print(get_file_content("calculator", "main.py"))
    print()

    print("Test 3: pkg/calculator.py")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    print("Test 4: /bin/cat (outside working directory)")
    print(get_file_content("calculator", "/bin/cat"))
    print()

    print("Test 5: pkg/does_not_exist.py (file does not exist)")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print()

if __name__ == "__main__":
    main()