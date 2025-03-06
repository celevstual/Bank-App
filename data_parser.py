from user_info import UserInfo
from admin_info import AdminManager

class UserDataParser:
    @staticmethod
    def parse_file_lines(lines):
        """Parse user information from the lines."""
        return [UserDataParser.parse_user_line(line) for line in lines if UserDataParser.parse_user_line(line)]

    @staticmethod
    def parse_user_line(line):
        """Parse a single line of user data."""
        parts = [part.strip() for part in line.split(',')]
        access_card, user_username, user_password = parts[:3]
        first_name = parts[3] if len(parts) > 3 else None
        last_name = parts[4] if len(parts) > 4 else None
        
        user = UserInfo(access_card, user_username, user_password, first_name, last_name)

        index = 5
        while index + 1 < len(parts):
            account_number, balance = parts[index:index + 2]
            if balance.startswith("$"):
                user.add_account(account_number, balance)
            index += 2

        for card_number in parts[index:]:
            if len(card_number) == 10 and card_number[0] in "89":
                user.add_card(card_number)

        user.associate_accounts_with_cards()

        return user

    @staticmethod
    def read_user_info_from_file(file_path):
        """Read user information from a file."""
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return UserDataParser.parse_file_lines(lines)
    
class AdminDataParser:
    """
    A class to parse admin data from a file and create AdminManager instances.
    """
    
    @staticmethod
    def parse_admin_file(file_path):
        """Read admin credentials from a file."""
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            return [AdminDataParser.parse_admin_line(line) for line in lines if line.strip()]
        except FileNotFoundError:
            print("Admin data file not found.")
            return []
    
    @staticmethod
    def parse_admin_line(line):
        """Parse a single line of admin credentials."""
        parts = [part.strip() for part in line.split(',')]
        if len(parts) < 2:
            print("Invalid admin data format.")
            return None
        admin_username, admin_password = parts[:2]
        AdminManager.create_admin_credentials(admin_username, admin_password)
        return admin_username