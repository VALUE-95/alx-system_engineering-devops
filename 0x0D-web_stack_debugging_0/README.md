## Webstack Debugging #0 Breakdown and Scripting

This prompt provides an introduction to a web stack debugging series where you'll learn to fix broken systems using Bash scripts.

### Scenario:

The task is to ensure a server has the following:

1. A copy of **/etc/passwd** in **/tmp**
2. A file named **/tmp/isworking** containing the string "OK"

These are essential for your web application to function.

### Steps to Fix Manually (**docker exec** commands):

1. **List files in /tmp**: `ls /tmp/`
2. **Copy /etc/passwd to /tmp**: `cp /etc/passwd /tmp/`
3. **Create /tmp/isworking**: `echo OK > /tmp/isworking`
4. **List files in /tmp again**: `ls /tmp/` (This verifies the fix)

### Scripting the Fix:

Here's the Bash script that automates these steps:

```bash
#!/usr/bin/env bash

# Fix the server by copying /etc/passwd and creating /tmp/isworking
cp /etc/passwd /tmp/
echo OK > /tmp/isworking

# Script explanation (optional, can be commented out)
# - The first line specifies the interpreter for the script (bash).
# - The commands copy the password file and create the "OK" file in /tmp.
```

**Explanation of Script Elements:**

- `#!/usr/bin/env bash`: Defines the interpreter for the script.
- `#`: Starts a comment line (ignored during execution).
- `cp /etc/passwd /tmp/`: Copies the password file.
- `echo OK > /tmp/isworking`: Creates the "OK" file.

**Remember:**

- Save the script with a filename ending in `.sh` (e.g., `fix_server.sh`).
- Make the script executable using `chmod +x fix_server.sh`.

This script should fix the server automatically when executed.
