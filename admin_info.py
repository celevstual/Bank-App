from cryptography.fernet import Fernet
from encryption import EncryptionManager

class AdminManager:
    """
    Manages admin authentication with encrypted passwords.
    """

    _admin_credentials = {}  # Stores admin usernames and encrypted passwords

    @classmethod
    def add_admin(cls, admin_username, admin_password):
        """
        Stores an admin's credentials with an encrypted password.
        """
        encrypted_password = EncryptionManager.encrypt_password(admin_password)
        cls._admin_credentials[admin_username] = encrypted_password

    @classmethod
    def authenticate_admin(cls, admin_username, admin_password):
        """
        Authenticates an admin by comparing decrypted passwords.
        """
        encrypted_password = cls._admin_credentials.get(admin_username)
        if encrypted_password:
            decrypted_password = EncryptionManager.decrypt_password(encrypted_password)
            return decrypted_password == admin_password
        return False

    @classmethod
    def get_admins(cls):
        """
        Returns a list of all stored admin usernames.
        """
        return list(cls._admin_credentials.keys())