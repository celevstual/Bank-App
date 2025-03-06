# user_info.py
from encryption import EncryptionManager

# Class to identify card type
class Card:
    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = self.identify_card_type()
        self.associated_accounts = []

    def identify_card_type(self):
        """Identify the card type based on the first digit."""
        card_types = {'8': 'Debit', '9': 'Credit'}
        return card_types.get(self.card_number[0], 'Unknown')

    def __str__(self):
        return f"{self.card_type} Card: {self.card_number}"

# Class to identify account type
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = self.identify_account_type()

    def identify_account_type(self):
        """Identify the account type based on the last digit."""
        return "Chequing" if self.account_number[-1] in "02468" else "Saving"

    def __str__(self):
        return f"{self.account_type} Account: {self.account_number}, Balance: {self.balance}"

# Class with all user information 
class UserInfo:
    _users = {}  # Stores users by both username and access card number

    def __init__(self, access_card=None, username=None, password=None, name=None, last_name=None):
        self.username = username
        self.password = self.encrypt_password(password) if password else None
        self.name = name
        self.last_name = last_name
        self.access_card = Card(access_card) if access_card else None
        self.accounts = []
        self.cards = []
        if self.access_card:
            self.cards.append(self.access_card)

        # Store user in lookup dictionaries
        if username:
            UserInfo._users[username] = self
        if access_card:
            UserInfo._users[access_card] = self

    def encrypt_password(self, password):
        """Encrypt the user's password."""
        return EncryptionManager.encrypt_password(password)

    def verify_password(self, input_password):
        """Verify the input password matches the stored encrypted password."""
        decrypted_password = EncryptionManager.decrypt_password(self.password)
        return decrypted_password == input_password

    def add_account(self, account_number, balance):
        """Add an account to the user."""
        self.accounts.append(Account(account_number, balance))

    def add_card(self, card_number):
        """Add a card to the user."""
        self.cards.append(Card(card_number))

    def associate_accounts_with_cards(self):
        """Associate accounts with cards based on matching prefixes."""
        for account in self.accounts:
            for card in self.cards:
                if account.account_number[:3] == card.card_number[:3]:
                    card.associated_accounts.append(account.account_number)

    @classmethod
    def authenticate(cls, identifier, password):
        """
        Authenticate a user using either a username or access card.
        """
        user = cls._users.get(identifier)
        if user and user.verify_password(password):
            return user
        return None

    def __str__(self):
        result = [
            f"User: {self.name} {self.last_name} ({self.username})",
            f"Access Card: {self.access_card}" if self.access_card else "Access Card: None",
        ]
        result.append("Accounts:")
        result.extend([f"  - {str(account)}" for account in self.accounts])
        result.append("Cards:")
        result.extend([f"  - {str(card)}" for card in self.cards])
        result.append("Card-Account Associations:")
        for card in self.cards:
            result.append(f"  {str(card)} -> {card.associated_accounts}")
        return "\n".join(result)