import multiprocessing

# Function to print numbers from 1 to n
def print_numbers(n):
    for i in range(1, n + 1):
        print(f"Number: {i}")

# Function to print letters from 'a' to 'n'
def print_letters(n):
    for letter in range(ord('a'), ord('a') + n):
        print(f"Letter: {chr(letter)}")

if __name__ == "__main__":
    
    process1 = multiprocessing.Process(target=print_numbers, args=(5,))
    process2 = multiprocessing.Process(target=print_letters, args=(5,))

    
    process1.start()
    process2.start()

 
    process1.join()
    process2.join()

    print("Both processes have finished.")
