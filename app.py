import sys
import signal

from src.ui.interface import GradioApp


def handle_shutdown(signal, frame):
    print(f"Singal {signal} received, shutting down gracefully...")
    sys.exit(0)

def main():
    # Register the signal handler for graceful shutdown
    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)
    signal.signal(signal.SIGTSTP, handle_shutdown)

    app = GradioApp(
        title ="Verity",
        description = "Uncover the truth in your documents"
    )
    app.demo.launch(server_name="127.0.0.1", server_port=7071)


if __name__ == "__main__":
    main()
# def --- IGNORE ---