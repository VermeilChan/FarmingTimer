#!/bin/bash

echo "This script will help you set up the necessary dependencies to use FarmingTimer."

read -p "Do you want to continue with the setup? (y/n): " install_dependencies

if [[ "$install_dependencies" != "y" ]]; then
    echo "Exiting setup. No dependencies will be installed."
    exit 0
fi

read -p "Please enter your package manager (apt/dnf/pacman/zypper): " package_manager

case $package_manager in
    apt)
        sudo apt update -y
        sudo apt install libxcb-cursor0 python3 python3-pip python3-venv -y
        ;;
    dnf)
        sudo dnf update -y
        sudo dnf install xcb-util-cursor python3 python3-pip python3-virtualenv -y
        ;;
    pacman)
        sudo pacman -Syu --noconfirm
        sudo pacman -S xcb-util-cursor python python-pip python-virtualenv --noconfirm
        ;;
    zypper)
        sudo zypper update
        sudo zypper install -y libxcb-cursor0 python3 python3-pip python3-virtualenv
        ;;
    *)
        echo "Error: Unsupported package manager. Please install Python 3, pip, venv, and libxcb manually."
        exit 1
        ;;
esac

python3 -m venv farmtimer
source farmtimer/bin/activate

pip install -r requirements.txt || { echo "Failed to install Python packages."; deactivate; exit 1; }

deactivate

cat <<EOF

|-----------------------------------------|
|     Setup completed successfully.       |
| Now, please run the following command:  |
|             bash Run.sh                 |
|-----------------------------------------|

EOF
