import multiprocessing
import subprocess
import time


def open_text_editor():
    subprocess.run(["nano"])


if __name__ == "__main__":
    text_editor_process = multiprocessing.Process(
        target=open_text_editor, name="TextEditorProcess")
    text_editor_process.start()

    try:
        # Wait for 10 seconds
        time.sleep(10)

        # Terminate the process after 10 seconds
        text_editor_process.terminate()
        text_editor_process.join()

    except KeyboardInterrupt:
        # Handle keyboard interrupt (e.g., if the user manually terminates the script)
        print("Process terminated manually.")

    print("Script finished.")
