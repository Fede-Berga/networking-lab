# Networking Lab: From Bridges to VLANs

<p align="center">
  <img src="assets/network-diagram.svg" alt="Project Architecture" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Incus-orange?style=for-the-badge&logo=linux" alt="Platform">
  <img src="https://img.shields.io/badge/Language-Bash%20%7C%20Python-blue?style=for-the-badge&logo=gnu-bash" alt="Language">
  <img src="https://img.shields.io/badge/Status-Educational-green?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="License">
</p>

---

## 📖 About The Project

This project is a comprehensive, hands-on networking laboratory designed to teach the fundamentals of **Network Segmentation**. It is built on top of **Incus** (a modern system container manager) to simulate real-world hardware environments using lightweight Linux containers.

**What you will learn:**
1.  **Physical Segmentation (Legacy)**: How networks were separated using multiple physical interfaces and bridges.
2.  **Logical Segmentation (Modern)**: Moving to **VLANs (802.1Q)** and Trunking to run multiple networks on a single cable.
3.  **Services & Security**: Deploying a real 3-tier architecture (Web DMZ, Internal Client, Secured Database) and configuring routing/NAT.

The lab is fully scripted but designed to be studied step-by-step.

> **Note**: The detailed step-by-step lesson plan is available in Italian in [`lesson-plan.md`](./lesson-plan.md).

---

## 🏗 Architecture

The lab builds a classic 3-tier network topology:

*   **DMZ (VLAN 10)**: Contains a Python Flask Web Server exposed to the public.
*   **Internal (VLAN 20)**: Simulates an employee workstation.
*   **Database (VLAN 30)**: A secured PostgreSQL database, accessible only by specific rules.
*   **Router**: An Alpine Linux container acting as the gateway/firewall for all networks.

---

## 🚀 Getting Started

This lab relies on **Incus** (or LXD), which requires a Linux kernel with bridge and VLAN support.

### 🐧 Linux (Native)
This is the recommended way to run the lab.

1.  **Install Incus**:
    Follow the official instructions for your distro (e.g., `apt install incus` or `snap install incus`).
    ```bash
    # Initialize Incus (accept defaults usually works)
    incus admin init
    ```

2.  **Clone this repo**:
    ```bash
    git clone https://github.com/your-username/networking-lab.git
    cd networking-lab
    ```

3.  **Run the Lab**:
    ```bash
    # 1. Setup the environment
    sudo bash scripts/setup_incus.sh
    
    # 2. Deploy the VLAN infrastructure
    sudo bash scripts/deploy_lab.sh
    ```

### 🪟 Windows
Incus **does not run natively on Windows**. You must use a Linux VM or WSL2.

**Option A: WSL2 (Recommended)**
1.  Install a distro like Ubuntu 22.04/24.04 from the Microsoft Store.
2.  Ensure Systemd is enabled in WSL2 (Create `/etc/wsl.conf` with `[boot] systemd=true`).
3.  Follow the **Linux** instructions above inside your WSL terminal.

**Option B: Virtual Machine**
1.  Install VirtualBox, VMware, or Hyper-V.
2.  Create a Linux VM (Ubuntu Server recommended).
3.  Follow the **Linux** instructions inside the VM.

### 🍎 macOS
Incus **does not run natively on macOS**. You need a Linux environment.

**Option A: OrbStack / Lima (Lightweight)**
1.  Install [OrbStack](https://orbstack.dev/) or `limactl`.
2.  Spin up a Linux machine.
3.  Follow the **Linux** instructions inside that machine.

**Option B: Virtual Machine**
1.  Use UTM or Parallels to run a Linux VM.
2.  Follow the **Linux** instructions inside the VM.

---

## 🛠 Usage

Once the lab is running:

1.  **Verify Status**:
    ```bash
    incus list
    ```
    You should see `router`, `web-server`, `workstation`, and `database` running.

2.  **Test Connectivity**:
    From the internal workstation, check if you can reach the DMZ web app:
    ```bash
    incus exec workstation -- curl http://10.10.1.10/health
    ```
    *Expected output: JSON response confirming connection to the Database.*

3.  **Cleanup**:
    To destroy the lab and free resources:
    ```bash
    sudo bash scripts/cleanup.sh
    ```

## 📂 Project Structure

*   `app/`: Source code for the Flask Web Application.
*   `config/`: Configuration files (e.g., `nftables` rules).
*   `scripts/`: Automation scripts for setting up and tearing down the lab.
*   `lesson-plan.md`: **The core educational content (Italian)** explaining every command in detail.

---

## 📜 License

The code and the lesson material are licensed separately:

*   The lesson material ([`lesson-plan.md`](lesson-plan.md) and the diagram in [`assets/`](assets/)) is licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0), see [`LICENSE-docs`](LICENSE-docs). You can reuse and adapt it, also in your own classes, as long as you credit Federico Bergamini.
*   Everything else, including the code in `app/`, `config/` and `scripts/`, is released under the [MIT License](LICENSE).
