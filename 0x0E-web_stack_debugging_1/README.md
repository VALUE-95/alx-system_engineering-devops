## 0x0E. Web stack debugging # - Debugging Nginx on Ubuntu Container

Here's how to solve the challenge in two Bash scripts:

**0-nginx_likes_port_80 (Longer Version):**

```bash
#!/usr/bin/env bash

# Check if Nginx is running
if ! service nginx status | grep running >/dev/null 2>&1; then
  # Start Nginx if not running
  service nginx start
fi

# Check configuration for port 80
grep -qE '^listen *:80' /etc/nginx/nginx.conf
if [[ $? -ne 0 ]]; then
  # Update configuration to listen on port 80
  sed -i 's/listen 80[^;]*/listen 80;/' /etc/nginx/nginx.conf
  # Reload Nginx configuration
  service nginx reload
fi
```

**1-debugging_made_short (Shorter Version):**

```bash
#!/usr/bin/env bash

! service nginx status | grep running && service nginx start
! grep -qE '^listen *:80' /etc/nginx/nginx.conf && sed -i 's/listen 80[^;]*/listen 80;/' /etc/nginx/nginx.conf && service nginx reload
```

**Explanation:**

1. **0-nginx_likes_port_80:**
   - Checks if Nginx is running using `service nginx status`.
   - If not running, starts it with `service nginx start`.
   - Greps the configuration file `/etc/nginx/nginx.conf` for `listen *:80`.
   - If not found, updates the configuration using `sed` to listen on port 80.
   - Reloads the configuration with `service nginx reload`.

2. **1-debugging_made_short (Advanced):**
   - This script combines the checks and fixes in one line using logical operators (`&&`) but adheres to the challenge's restrictions.
      - Starts Nginx if not running (`! service nginx status | grep running && service nginx start`).
      - Updates configuration and reloads only if `listen *:80` is missing (`! grep -qE '^listen *:80' /etc/nginx/nginx.conf && ...`).

**Note:**

- Remember to replace `0:80` with the actual container IP address in your `curl` command for verification.
- These scripts assume a basic Nginx configuration. You might need adjustments for more complex setups.
