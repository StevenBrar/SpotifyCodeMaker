
# Spotify Code Maker

Generate **Spotify Codes** for every track in a playlist using Python + Spotify’s Web API.  

Perfect for printing, sharing, or embedding in projects.



## Features
- Fetches all tracks from a public Spotify playlist (will have feature in future for private playlists)
- Generates Spotify Code images for each track
- Saves codes as `.png`, `.jpeg`, or `.svg` with custom background & code colors
- Skips duplicates automatically
- Optional `.env` support for API keys (no more messing with environment variables)
## Set-Up

### 1. Clone the repo

git clone https://github.com/StevenBrar/SpotifyCodeMaker.git
cd SpotifyCodeMaker

### 2. Install dependencies
bash-
pip install -r requirements.txt

### 3. Get Spotify API credentials
Go to Spotify Developer Dashboard
Create a new App
Copy your Client ID and Client Secret

### 4. Configure secrets
Create a .env file in the project root:

ini-
SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here


## Usage

Run the script with a Spotify playlist link:

Example: 

playlist_to_codes("https://open.spotify.com/playlist/7kuA3yIM1X3Y7i38m0iNcb?si=193de1366f2644ce")

bash-

python playlist_to_spotify_codes.py

By default, codes are saved to the spotify_codes/ folder.
## Example Output

```
spotify_codes/
├── Artist1 - Song1.png
├── Artist2 - Song2.png
└── Artist3 - Song3.png
```
