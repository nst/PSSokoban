import os
import termios
import tty
import sys

def main():
    pipe_path = "/tmp/p"

    if not os.path.exists(pipe_path):
        print(f"Named pipe {pipe_path} does not exist.")
        return

    print(f"Type PostScript commands interactively (Ctrl+C to quit):\nPipe: {pipe_path}")

    orig_settings = termios.tcgetattr(sys.stdin)

    try:
        tty.setraw(sys.stdin.fileno())

        with open(pipe_path, 'w') as pipe:
            while True:
                char = sys.stdin.read(1)

                if char == '\x03':  # Ctrl+C
                    break

                pipe.write(f"{char}\n")
                pipe.flush()

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)

if __name__ == "__main__":
    main()
