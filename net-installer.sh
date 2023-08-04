#!/bin/bash


NAUTILUS_PATH=$(which nautilus)
TMP_DIR=$(mktemp --directory)

download() {
  curl -s 'https://api.github.com/repos/chr314/nautilus-copy-path/releases/latest' | jq -r '.tarball_url' | wget -i - -O nautilus-copy-path.tar.gz
  tar -xzf nautilus-copy-path.tar.gz --strip-components=1
}

install () {
  mkdir -p ~/.local/share/nautilus-python/extensions/nautilus-copy-path
  cp nautilus-copy-path.py ~/.local/share/nautilus-python/extensions
  cp nautilus_copy_path.py translation.py config.json ~/.local/share/nautilus-python/extensions/nautilus-copy-path
  cp -rf translations ~/.local/share/nautilus-python/extensions/nautilus-copy-path
  "${NAUTILUS_PATH}" -q || true
}

install_dependencies() {
  DNF_CMD=$(which dnf)
  APT_GET_CMD=$(which apt-get)
  PACMAN_CMD=$(which pacman)

  if [[ -n $DNF_CMD ]]; then
    dnf -y install nautilus-python python3-gobject
  elif [[ -n $APT_GET_CMD ]]; then
    apt-get -y install python3-nautilus python3-gi
  elif [[ -n $PACMAN_CMD ]]; then
    pacman -S python-nautilus python-gobject --noconfirm
  fi
}

clear_exit() {
  rm -rf "${TMP_DIR}"
  exit 0
}

error_exit() {
  echo "${1}"
  rm -rf "${TMP_DIR}"
  exit 1
}

cd "${TMP_DIR}" || error_exit 'Failed to change directory'

install_dependencies || error_exit 'Failed to install dependencies'
download || error_exit 'Failed to download nautilus-copy-path'
install || error_exit 'Failed to install nautilus-copy-path'

echo 'nautilus-copy-path installed successfully'

clear_exit