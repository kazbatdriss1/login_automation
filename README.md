# login_automation
# Automation Script for Environment Setup and Logins

This project contains scripts to automate the setup of a development environment and login to various web services.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Scripts](#scripts)

## Prerequisites

Ensure you have the following installed:

- **GNOME** desktop environment
- **VS Code**
- **Python 3**
- **Google Chrome**
- **ChromeDriver** (compatible with your version of Google Chrome)

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python packages:
    ```bash
    pip install selenium
    ```

## Usage

1. Make the shell script executable:
    ```bash
    chmod +x setup_environment.sh
    ```

2. Run the shell script to set up the environment and install VS Code extensions:
    ```bash
    ./setup_environment.sh
    ```

3. Configure your login credentials in the Python script `login_automation.py`.

4. Run the Python script to automate the logins:
    ```bash
    python3 login_automation.py
    ```

## Configuration

Edit the `login_automation.py` file to set your login credentials:

```python
github_username = "your_github_username"
github_password = "your_github_password"
zone_username = "your_zone01oujda_username"
zone_password = "your_zone01oujda_password"
spotify_username = "your_spotify_username"
spotify_password = "your_spotify_password"
