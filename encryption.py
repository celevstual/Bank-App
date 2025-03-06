from cryptography.fernet import Fernet

class EncryptionManager:
    """
    A class to manage encryption and decryption of passwords using the Fernet symmetric encryption scheme.
    It also handles the generation and loading of encryption keys.
    """

    KEY_FILE = 'secret.key'
    CREDENTIALS_FILE = 'admin_credentials.txt'

    @staticmethod
    def generate_key():
        """Generate and save a key to 'secret.key'."""
        key = Fernet.generate_key()
        with open(EncryptionManager.KEY_FILE, 'wb') as key_file:
            key_file.write(key)
        print(f"Key generated and saved as '{EncryptionManager.KEY_FILE}'.")

    @staticmethod
    def load_key():
        """Load the key from 'secret.key'."""
        try:
            with open(EncryptionManager.KEY_FILE, 'rb') as key_file:
                return key_file.read()
        except FileNotFoundError:
            print("Key file not found. Please generate a key first.")
            return None

    @staticmethod
    def encrypt_password(password):
        """Encrypt a password using the loaded key."""
        key = EncryptionManager.load_key()
        if not key:
            raise ValueError("Encryption key not found. Please generate a key first.")
        f = Fernet(key)
        return f.encrypt(password.encode('utf-8'))

    @staticmethod
    def decrypt_password(encrypted_password):
        """Decrypt a password using the loaded key."""
        key = EncryptionManager.load_key()
        if not key:
            raise ValueError("Encryption key not found. Please generate a key first.")
        f = Fernet(key)
        return f.decrypt(encrypted_password).decode('utf-8')

    @staticmethod
    def create_admin_credentials(username, password):
        """Create and save admin credentials with an encrypted password."""
        encrypted_password = EncryptionManager.encrypt_password(password)
        with open(EncryptionManager.CREDENTIALS_FILE, 'w') as file:
            file.write(f"{username}\n")
            file.write(encrypted_password.decode('utf-8'))
        print("Admin credentials created successfully!")

    @staticmethod
    def load_admin_credentials():
        """Load and decrypt admin credentials from the file."""
        try:
            with open(EncryptionManager.CREDENTIALS_FILE, 'r') as file:
                stored_username = file.readline().strip()
                stored_encrypted_password = file.readline().strip().encode('utf-8')

            stored_password = EncryptionManager.decrypt_password(stored_encrypted_password)
            return stored_username, stored_password
        except FileNotFoundError:
            raise FileNotFoundError("Admin credentials not found. Please create an admin account first.")

    @staticmethod
    def verify_admin_login(username, password):
        """Verify the admin login credentials."""
        try:
            stored_username, stored_password = EncryptionManager.load_admin_credentials()
            return username == stored_username and password == stored_password
        except Exception as e:
            print(f"Error: {e}")
            return False