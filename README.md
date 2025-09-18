# SpotifyCodeMaker 

Generate **Spotify Codes** for every track in a playlist using Python + Spotify’s Web API.  
Perfect for printing, sharing, or embedding in projects.

---

## Features
- Fetches all tracks from a public (or private) Spotify playlist
- Generates Spotify Code images for each track
- Saves codes as `.png`, `.jpeg`, or `.svg` with custom background & code colors
- Skips duplicates automatically
- Optional `.env` support for API keys (no more messing with environment variables)

---

## 🛠️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/StevenBrar/SpotifyCodeMaker.git
cd SpotifyCodeMaker

2. Install dependencies

pip install -r requirements.txt 

3. Get Spotify API credentials

    Go to Spotify Developer Dashboard

    Create a new app

    Copy your Client ID and Client Secret

4. Configure secrets

Create a .env file in the project root:

SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here

▶️ Usage

Run the script with a Spotify playlist link:

python playlist_to_spotify_codes.py

By default, codes are saved to the spotify_codes/ folder.
⚙️ Customization

In playlist_to_spotify_codes.py you can tweak:

CODES_FORMAT = "png"   # "png", "jpeg", "svg"
BG_HEX = "000000"      # background color (hex without #)
CODE_COLOR = "white"   # "white" or "black"
SIZE = "640"           # image size (80–640)

📂 Example Output

spotify_codes/
├── Artist1 - Song1.png
├── Artist2 - Song2.png
└── Artist3 - Song3.png