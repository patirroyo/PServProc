"""Exercise 3: List all process in operative system with PID, and allow termination of one by PID"""

import psutil

def list_processes():
    print("List of processes:")
    for process in psutil.process_iter(['pid', 'name']):
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}")

def terminate_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"Process with PID {pid} terminated successfully.")
    except psutil.NoSuchProcess as e:
        print(f"Error: {e}")
    except psutil.AccessDenied as e:
        print(f"Error: {e}")

def main():
    while True:
        print("\nOptions:")
        print("1. List all processes")
        print("2. Terminate a process by PID")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            list_processes()
        elif choice == "2":
            try:
                pid_to_terminate = int(input("Enter the PID of the process to terminate: "))
                terminate_process(pid_to_terminate)
            except ValueError:
                print("Invalid input. Please enter a valid PID.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
