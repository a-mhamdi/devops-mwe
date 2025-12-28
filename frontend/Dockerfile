FROM node:alpine

# Create app directory
WORKDIR /usr/src/app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install --only=production

# Copy app source
COPY . .

# Create non-root user
RUN adduser -S -u 1001 -G users mhamdi
RUN chown -R mhamdi:users /usr/src/app
USER mhamdi

# Expose port
EXPOSE 3000

# Start the application
CMD ["node", "server.js"]
