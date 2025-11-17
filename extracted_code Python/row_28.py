def repl():
    while True:
        try:
            # Read a line of input from the user
            user_input = input("REPL> ")
            
            # Evaluate the user's input using eval()
            if user_input:  # Check if the input is not empty
                result = eval(user_input)
                print(result)
        except Exception as e:
            # Handle any exceptions that occur during evaluation
            print(f"Error: {e}")
        except KeyboardInterrupt:
            # Handle keyboard interrupt to exit gracefully
            print("\nExiting REPL...")
            break

if __name__ == "__main__":
    repl()