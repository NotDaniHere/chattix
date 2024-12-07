from datetime import datetime

class ChatUtility:
    """
    Provides utility functions for the chatroom.
    """

    @staticmethod
    def format_message(username, message):
        """
        Formats a message with a timestamp.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {"timestamp": timestamp, "username": username, "message": message}

    @staticmethod
    def validate_message(data):
        """
        Validates the incoming message data. Checks for username and message presence.
        """
        if not isinstance(data, dict):
            return False, "Invalid data format"
        if "username" not in data or "message" not in data:
            return False, "Missing username or message"
        if not data["username"] or not data["message"]:
            return False, "Empty username or message"
        return True, "Valid data"

    @staticmethod
    def sanitize_input(text):
        """
        Sanitizes user input to prevent malicious content.
        """
        return text.strip().replace("<", "&lt;").replace(">", "&gt;")
