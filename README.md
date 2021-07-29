# tracklist_formatter
Quick script to format Traktor html playlists as Artist - Title [Label]


## Setup
1. Click the green box in the upper right that says "Code"
2. Choose Download ZIP
3. Unzip the folder and move the file `tracklist_formatter.py` to the folder where you save your html playlists

## Usage
1. Open Terminal
2. Navigate to the folder where `tracklist_formatter.py` is stored using cd (see here for a tutorial: https://www.macworld.com/article/221277/command-line-navigating-files-folders-mac-terminal.html)
3. Run the script by entering `python tracklist_formatter.py my_tracklist.html`. If your playlist name has spaces in it, be sure to put quotation marks around it like `python tracklist_formatter.py "my tracklist.html"`. If it's stored in a subfolder, include that like `python tracklist_formatter.py "my folder/my tracklist.html"`. The `.html` is optional, it should work if you leave it off.
4. It should print out your tracklist as text. If there's an error, it should tell you what is wrong. If nothing happens, that means there's a bug somewhere so please let me know!
5. If you would rather have it as a file, you can add `> my_pretty_tracklist.txt` to the end of your command above. Nothing will print in this case, and that's ok as long it shows up in the file.
