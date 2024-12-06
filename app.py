import json
from flask import Flask, request, render_template, redirect, url_for

# Initialize Flask app
app = Flask(__name__)

# File paths
USER_PROFILES_PATH = "user_profiles.json"
BANNED_USERS_PATH = "banned_users.json"

# Load existing JSON data
def load_json(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save JSON data
def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

# Load user data
user_profiles = load_json(USER_PROFILES_PATH)
banned_users = load_json(BANNED_USERS_PATH)

# Mock list of online users (would normally be updated dynamically)
online_users = [""]  # Example online users


@app.route("/")
def index():
    """Main page with navigation buttons."""
    return render_template("index.html")


@app.route("/config", methods=["GET", "POST"])
def config():
    """Configuration management page."""
    if request.method == "POST":
        server_config = request.form.to_dict()
        save_json("config.json", server_config)
        return "Server configuration saved!", 200

    try:
        with open("config.json", "r") as f:
            config_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        config_data = {}

    return render_template("config.html", config=config_data)


@app.route("/users", methods=["GET", "POST"])
def manage_users():
    """User management page."""
    if request.method == "POST":
        # Handle adding new user
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password:
            user_profiles[username] = password
            save_json(USER_PROFILES_PATH, user_profiles)
            return f"User '{username}' added successfully!", 200
        return "Invalid input.", 400

    return render_template("users.html", users=user_profiles)


@app.route("/ban", methods=["GET", "POST"])
def ban_user():
    """Ban users from the server."""
    if request.method == "POST":
        username = request.form.get("username")
        if username in user_profiles and username not in banned_users:
            banned_users.append(username)
            save_json(BANNED_USERS_PATH, banned_users)
            return f"User '{username}' has been banned!", 200
        return f"User '{username}' not found or already banned.", 404

    # Check for online users
    has_online_users = bool(online_users)

    return render_template(
        "user_actions.html",
        action="Ban",
        users=user_profiles,
        online_users=online_users if has_online_users else None,
        has_online_users=has_online_users,
        banned_users=banned_users,
    )


@app.route("/kick", methods=["GET", "POST"])
def kick_user():
    """Kick users from the server."""
    if request.method == "POST":
        username = request.form.get("username")
        if username in online_users:
            online_users.remove(username)  # Simulate kicking the user
            return f"User '{username}' has been kicked!", 200
        return f"User '{username}' not found or already offline.", 404

    # Check for online users
    has_online_users = bool(online_users)

    return render_template(
        "user_actions.html",
        action="Kick",
        users=user_profiles,
        online_users=online_users if has_online_users else None,
        has_online_users=has_online_users,
        banned_users=banned_users,
    )
