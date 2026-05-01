FROM python:3.10-slim

# Install system utilities, git, and dependencies for downloading ttyd
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    nano \
    htop \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Download and install ttyd (Web Terminal)
RUN curl -sLk https://github.com/tsl0922/ttyd/releases/download/1.7.4/ttyd.x86_64 -o /usr/local/bin/ttyd \
    && chmod +x /usr/local/bin/ttyd

WORKDIR /app

# Expose the port ttyd will run on
EXPOSE 8080

# Run ttyd. We use environment variables for the username and password so they aren't hardcoded in this public file.
# The -W flag makes it writable, so you can type commands.
CMD ["sh", "-c", "ttyd -W -p 8080 -c ${TERMINAL_USER}:${TERMINAL_PASSWORD} bash"]
