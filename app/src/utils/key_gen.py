import string
import secrets


class KeyGenerator:
    @classmethod
    def generate_key(cls) -> str:
        char_len = 7
        chars = string.digits + string.ascii_lowercase + string.ascii_uppercase
        return "".join(secrets.choice(chars) for _ in range(char_len))
