# SpotifyCodeMaker 🎶➡️📷

Generate **Spotify Codes** for every track in a playlist using Python + Spotify’s Web API.  
Perfect for printing, sharing, or embedding in projects.

---

## ✨ Features
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


pip install -r requirements.txt

SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here

python playlist_to_spotify_codes.py

CODES_FORMAT = "png"   # "png", "jpeg", "svg"
BG_HEX = "000000"      # background color (hex without #)
CODE_COLOR = "white"   # "white" or "black"
SIZE = "640"           # image size (80–640)


spotify_codes/
├── Artist1 - Song1.png
├── Artist2 - Song2.png
└── Artist3 - Song3.png


---

### Next steps for you
1. Create a file `README.md` in your repo root.  
2. Paste the above content.  
3. Commit & push:
   ```powershell
   git add README.md
   git commit -m "Add README with setup and usage instructions"
   git push
