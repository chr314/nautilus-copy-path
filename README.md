# Nautilus Copy Path/Name

![ScreenShot](https://raw.githubusercontent.com/chr314/nautilus-copy-path/master/screenshot.png)

## Installation

###  [AUR](https://aur.archlinux.org/packages/nautilus-copy-path/)

#### With yay or yaourt
1. `yay -S nautilus-copy-path` or `yaourt -S nautilus-copy-path`
2. Restart the Nautilus (`nautilus -q`)

#### Or manual
1. `git clone https://aur.archlinux.org/nautilus-copy-path.git`
2. `cd nautilus`
3. `makepkg -si`
4. Restart the Nautilus (`nautilus -q`)


### Manual installation

#### Install Dependencies

Fedora `sudo dnf install nautilus-python python3-gobject`

Ubuntu `sudo apt install python-nautilus python3-gi`

#### Download & Install the Extension

1. `git clone https://github.com/chr314/nautilus-copy-path.git`

2. `cd nautilus-copy-path`

3. `make install`

4. Restart the Nautilus (`nautilus -q`)

## Uninstallation

1. `cd path/to/nautilus-copy-path`
   
2. `make uninstall`
   
3. Restart the Nautilus (`nautilus -q`)

## Currently supported languages 
- Chinese
- English
- French
- German
- Greek
- Italian
- Japanese
- Polish
- Portuguese
- Romanian
- Russian
- Spanish

#### Add new translations

Translations files are in `translations` directory

example: [English Translation](translations/en.json)

1. Copy the english translation file (`en.json`), the new file name must be the new language code (e.g. `es.json`)

2. Translate the values in the new file

3. Add information in the README in the section *Currently supported languages* about new language 

3. Create Pull Request with the new translation
