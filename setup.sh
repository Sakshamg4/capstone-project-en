#!/bin/bash
echo "🌱 Capstone Generator — Setup"
echo "============================="
python3 -m venv venv
source venv/bin/activate
pip install python-pptx python-docx lxml
echo "✅ Python ready"
cd server && npm install && cd ..
cd client && npm install && cd ..
echo "✅ Node ready"
if [ -z "$(grep -v '^GROQ_API_KEY=$' .env | grep GROQ_API_KEY)" ]; then
  echo "⚠️  Add Groq key to .env → https://console.groq.com"
fi
echo "🎉 Run: ./start.sh"
