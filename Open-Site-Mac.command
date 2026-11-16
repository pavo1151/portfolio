#!/bin/bash
# Double-click to open the site (macOS). Keep this window open while browsing.
cd "$(dirname "$0")"
PORT=8765
open "http://localhost:$PORT/" 2>/dev/null &
python3 -m http.server $PORT --bind 127.0.0.1
