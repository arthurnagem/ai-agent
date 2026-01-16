from functions.write_file import write_file

def main():
    print("Test 1: Overwrite 'lorem.txt' in calculator")
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    print()

    print("Test 2: Write 'morelorem.txt' in pkg subdirectory")
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    print()

    print("Test 3: Attempt to write outside working directory (/tmp/temp.txt)")
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)
    print()

if __name__ == "__main__":
    main()