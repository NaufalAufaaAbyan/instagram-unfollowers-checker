from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# Nama folder yang berisi file JSON
FOLDER_NAME = "files_json"

def load_json(file_name):
    """Memuat data JSON dari sebuah file."""
    file_path = os.path.join(FOLDER_NAME, file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' tidak ditemukan di folder '{FOLDER_NAME}'.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{file_name}' berisi JSON yang tidak valid.")
        return None

def extract_usernames(data, key=None):
    """Mengekstrak username dari data JSON."""
    if key:
        data = data.get(key, [])
    return [item["string_list_data"][0]["value"].strip() for item in data]

def find_unfollowers(followers, following):
    """Mencari pengguna yang tidak mengikuti balik."""
    return list(set(following) - set(followers))

def find_not_following_back(followers, following):
    """Mencari pengguna yang tidak Anda ikuti kembali."""
    return list(set(followers) - set(following))

@app.route('/')
def index():
    # Nama file JSON
    followers_json_name = "followers_1.json"
    following_json_name = "following.json"

    # Memuat data JSON
    followers_data = load_json(followers_json_name)
    following_data = load_json(following_json_name)

    # Jika data tidak valid, tampilkan pesan error
    if not followers_data or not following_data:
        return "Error: File JSON tidak ditemukan atau tidak valid."

    # Mengekstrak username
    followers = extract_usernames(followers_data)
    following = extract_usernames(following_data, "relationships_following")

    # Mencari pengguna yang tidak mengikuti balik
    unfollowers = find_unfollowers(followers, following)

    # Mencari pengguna yang tidak Anda ikuti kembali
    not_following_back = find_not_following_back(followers, following)

    # Menampilkan hasil di template HTML
    return render_template(
        'index.html',
        following_count=len(following),
        followers_count=len(followers),
        unfollowers_count=len(unfollowers),
        not_following_back_count=len(not_following_back),
        unfollowers=unfollowers,
        not_following_back=not_following_back
    )

if __name__ == "__main__":
    app.run(debug=True)