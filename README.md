# Bank-App

This project is a Bank Account Management System implemented in Python. It includes user authentication, customer operations, and admin operations.

## Features
- **User Authentication**: Users must log in with their account number and password to access their accounts. Passwords are securely stored in the database.
- **Customer Operations**:
  - Check account balance
  - Deposit funds
  - Withdraw funds
  - Transfer funds to other accounts within the bank
  - Change account password
- **Admin Operations**:
  - Create new customer accounts
  - Update customer account details
  - Delete customer accounts
  - Search for customer accounts by account number or account holder's name
  - View a list of all customer accounts
- **File Handling**: All changes and additions/removals are updated in the file each time the program is run.
- **Graphical User Interface (GUI)**: The program includes a user-friendly GUI using Tkinter.

## Bonus Features
- **Encryption**: Passwords are encrypted for added security.
- **Multiple Accounts**: Customers can have more than one account and choose between them for operations.

## Setup
1. **Install the required libraries**:
   ```bash
   pip install cryptography
   pip install tkinter

## License
This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**. This license ensures that any modifications to the code must also be open source and distributed under the same license. It also includes a clause that requires anyone who uses the code over a network to make the source code available to their users.
