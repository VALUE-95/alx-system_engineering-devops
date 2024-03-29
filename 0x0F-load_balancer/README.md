## 0x0F. Load balancer - Load Balancing with HAProxy

**Project Overview**

This project aims to enhance the redundancy and scalability of your web infrastructure by implementing a load balancer with HAProxy. Here, we'll configure a dedicated server (gc-[STUDENT_ID]-lb-01-XXXXXXXXXX) to distribute incoming traffic across two web servers (517026-web-01 and gc-[STUDENT_ID]-web-02-XXXXXXXXXX).

**Project Goals**

* Achieve redundancy in the web server layer.
* Increase traffic handling capacity by distributing requests across multiple servers.
* Automate load balancer configuration for efficiency.

**Requirements**

* **Scripting Language:** Bash
* **Text Editor:** vi, vim, or emacs
* **Target OS:** Ubuntu 16.04 LTS
* **Script Naming Convention:** `<filename>.sh` (all scripts must end with a new line)
* **Documentation:** README.md (at project root)
* **Script Permissions:** Executable
* **Shellcheck Compliance:** No errors with Shellcheck (version 0.3.7)
* **Script Header:**
    * Line 1: `#!/usr/bin/env bash`
    * Line 2: Comment explaining script functionality

**Timeline**

* **Project Start:** March 28, 2024, 6:00 AM
* **Checker Release:** March 29, 2024, 12:00 PM
* **Project Deadline:** April 2, 2024, 6:00 AM (Auto Review)

**Steps**

1. **Load Balancer Server Preparation**
    * Access the new load balancer server (gc-[STUDENT_ID]-lb-01-XXXXXXXXXX).
    * Update and upgrade system packages with a script (e.g., `update_and_upgrade.sh`).
    * Install HAProxy using a script (e.g., `install_haproxy.sh`).

2. **HAProxy Configuration**
    * Create a configuration file (`/etc/haproxy/haproxy.cfg`) that defines:
        * Frontend section: Port for receiving traffic (e.g., port 80).
        * Backend section: Pool of web servers (including health checks).
        * Load balancing strategy (e.g., round-robin).

3. **Bash Script Automation**
    * Develop a script (e.g., `configure_haproxy.sh`) to automate the configuration process, including:
        * Calling update/upgrade script.
        * Installing HAProxy.
        * Creating and populating the HAProxy configuration file.
        * Restarting the HAProxy service for changes to take effect.

4. **Testing and Verification**
    * Verify HAProxy is running and listening on the designated port.
    * Simulate traffic to the load balancer's IP and port to confirm request distribution.

5. **Documentation**
    * Create this README.md file to provide an overview of the project, including:
        * Project goals
        * Steps taken
        * Script functionalities
        * Instructions for running the scripts

**Additional Notes**

* Consider implementing advanced HAProxy features like health checks and failover for enhanced reliability.
* Refer to the provided resources and HAProxy documentation for detailed configuration options.
* Ensure your scripts are well-commented and easy to understand.

**Resources**

* Introduction to load-balancing and HAProxy: [search load balancing introduction ON haproxy.com]
* HTTP header: [search http headers ON Mozilla developer.mozilla.org]
* Debian/Ubuntu HAProxy packages: [search install haproxy on ubuntu ON UpCloud upcloud.com]

This project provides valuable hands-on experience with DevOps practices by leveraging Bash scripting for server configuration automation and implementing HAProxy for load balancing. Remember to manage your time effectively and utilize the checker release for early feedback.
