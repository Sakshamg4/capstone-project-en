#!/bin/bash
source venv/bin/activate 2>/dev/null || true
DIR="$(cd "$(dirname "$0")" && pwd)"
echo "🌱 Backend → http://localhost:5000"
echo "   Frontend → http://localhost:3000"
cd "$DIR/server" && node index.js &
cd "$DIR/client" && npm run dev
