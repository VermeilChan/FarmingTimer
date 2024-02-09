#!/bin/bash

echo "This script will download the required dependencies to use FarmingTimer."

read -p "Do you want to continue with the setup? (y/n): " install_dependencies
echo

if [[ "$install_dependencies" != "y" ]]; then
    echo "Exiting setup. No dependencies will be installed."
    exit 0
fi
echo

read -p "Do you want to install the GUI version? (y/n): " install_xcb_libraries
echo

if [[ "$install_xcb_libraries" == "y" ]]; then
    read -p "Enter your package manager (apt/dnf/pacman/zypper): " package_manager
    echo

    case $package_manager in
        apt|dnf|pacman|zypper)
            ;;
        *)
            echo "Error: Invalid package manager. Please enter one of the following: apt, dnf, pacman, zypper."
            exit 1
            ;;
    esac
    echo

    echo "Please wait, downloading dependencies..."
    sudo "${package_manager}" update -y

    echo "Installing necessary libraries for GUI support..."
    case $package_manager in
        apt)
            sudo "${package_manager}" install libxcb-cursor0 -y
            ;;
        dnf)
            sudo "${package_manager}" install xcb-util-cursor -y
            ;;
        pacman)
            sudo "${package_manager}" -S xcb-util-cursor --noconfirm
            ;;
        zypper)
            sudo "${package_manager}" install -y libxcb-cursor0
            ;;
    esac
fi

echo "Installing Python 3, pip, and venv..."
case $package_manager in
    apt|dnf)
        sudo "${package_manager}" install python3 python3-pip python3-venv -y
        ;;
    pacman)
        sudo "${package_manager}" -S python python-pip python-virtualenv --noconfirm
        ;;
    zypper)
        sudo "${package_manager}" install -y python3 python3-pip python3-virtualenv
        ;;
    *)
        echo "Error: Unsupported package manager. Please install Python 3, pip, and venv manually."
        exit 1
        ;;
esac

echo "Creating and activating a virtual environment..."
python3 -m venv farmingtimer
source farmingtimer/bin/activate

echo "Installing Python packages from requirements.txt..."
pip install -r requirements.txt

echo "Deactivating the virtual environment..."
deactivate

cat <<EOF

|-----------------------------------------|
|     Setup completed successfully.       |
| Now, please run the following command:  |
|             bash Run.sh                 |
|-----------------------------------------|

EOF
