import sys
from importlib.metadata import version

from anthropic import Anthropic


def main():
    print("Python version:")
    print(sys.version)

    print("\nAnthropic SDK installation:")
    print(f"Anthropic SDK version: {version('anthropic')}")

    print("\nImport verification:")
    print("Anthropic client imported successfully.")

    print("\nInstallation verified.")


if __name__ == "__main__":
    main()
