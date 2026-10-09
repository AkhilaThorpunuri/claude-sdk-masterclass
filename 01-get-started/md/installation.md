# Installation

> Venkata Bhattaram (c) 2026

## Contents

- Checking the Python Version
- Creating a Python Virtual Environment
- Installing Dependencies
- Installing the Anthropic Python SDK
- Verifying the Installation
- Installation Checklist

## Overview

This Masterclass uses a shared Python environment for all lessons. The environment is configured once and reused throughout the tutorial.

The installation consists of:

- **Python 3.13** — the recommended Python version for this Masterclass.
- **Anthropic Python SDK** — the official Python library for interacting with Claude models.
- **Virtual Environment** — isolates project dependencies inside `.venv`.
- **Requirements File** — records the packages needed to reproduce the environment.

The Anthropic Python SDK requires Python 3.10 or later. Python 3.13 is selected as the recommended baseline for this Masterclass.


## 1. Check the Python Version

Check the Python versions installed on your machine:

```powershell
py --list
```

Check the active Python interpreter:

```powershell
python --version
```

For this Masterclass, Python 3.13 is the recommended baseline.

If Python 3.13 is installed, select it explicitly when creating the virtual environment.

If it is not installed, install Python 3.13 before proceeding.

## 2. Create a Virtual Environment

Open PowerShell in the root directory of the repository.

Create the virtual environment:

```powershell
py -3.13 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Verify the active interpreter:

```powershell
python --version
```

The terminal should display the `(.venv)` prefix when the virtual environment is active.

## 3. Install the Anthropic Python SDK

Install the official Claude SDK package:

```powershell
python -m pip install anthropic
```

Verify the installed package:

```powershell
python -m pip show anthropic
```

Verify that Python can import the SDK:

```powershell
python -c "from anthropic import Anthropic; print('Anthropic SDK imported successfully.')"
```

Expected output:

```text
Anthropic SDK imported successfully.
```

## 4. Verify the Installation

Create the following file:

```text
01-get-started/
└── code/
    └── verify_installation.py
```

Add this code to `verify_installation.py`:

```python
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
```

Run the script from the repository root:

```powershell
python 01-get-started/code/verify_installation.py
```

Expected output will resemble:

```text
Python version:
3.13.x ...

Anthropic SDK installation:
Anthropic SDK version: <installed-version>

Import verification:
Anthropic client imported successfully.

Installation verified.
```

## 5. Installation Checklist

Before proceeding to the next lesson, verify the following:

```text
[ ] Python 3.13 installed
[ ] Virtual environment created
[ ] Virtual environment activated
[ ] pip upgraded
[ ] Anthropic Python SDK installed
[ ] SDK import verified
[ ] verify_installation.py executed successfully
```
## Conclusion

The installation process for this Masterclass is:

```text
Python 3.13
     ↓
Virtual Environment
     ↓
Anthropic Python SDK
     ↓
Dependency Configuration
     ↓
Installation Verification
```

The core installation is complete when `verify_installation.py` prints:

```text
Installation verified.
```
