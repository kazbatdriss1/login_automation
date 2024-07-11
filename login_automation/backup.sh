#!/bin/bash

# Edit a settings of machine
gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'
gsettings set org.gnome.desktop.input-sources sources "[('xkb', 'us'), ('xkb', 'fr')]"
gsettings set org.gnome.shell.extensions.dash-to-dock extend-height false
gsettings set org.gnome.shell.extensions.dash-to-dock dock-position 'LEFT'
gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing'

pip install selenium

# Add extensions in Visual Studio Code
extensions=(
golang.go
ms-azuretools.vscode-docker
postman.postman-for-vscode
ritwickdey.liveserver
ms-python.python
)
for extension in "${extensions[@]}"; do
    code --install-extension "$extension"
done
# Run the Python script to login automatically
python3 login_automation.py

echo "successfully."
