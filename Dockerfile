FROM node:18-slim
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
RUN python3 -m venv venv && ./venv/bin/pip install python-pptx python-docx lxml
RUN cd server && npm install
RUN cd client && npm install && npm run build
ENV NODE_ENV=production
EXPOSE 5000
CMD ["node", "server/index.js"]
