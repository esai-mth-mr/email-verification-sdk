# Email Verification SDK

## Overview

This project provides an email validation service using the Hunter API. It includes an in-memory data storage system to manage email verification states. The service can validate email addresses, store their verification status, and retrieve this information.

## Features

- Validate email addresses using the Hunter API.
- Store and manage email verification states in memory.
- Simple and efficient API client for interacting with the Hunter API.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/esai-mth-mr/email-verification-sdk
   cd email-verification-sdk
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running mypy
```
mypy sdk/
```
