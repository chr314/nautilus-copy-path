# Nautilus Copy Path/Name

![ScreenShot](https://raw.githubusercontent.com/chr314/nautilus-copy-path/master/screenshot.png)

# Installation

##  [AUR](https://aur.archlinux.org/packages/nautilus-copy-path/)

1. `yay -S nautilus-copy-path` or `yaourt -S nautilus-copy-path`
2. Restart the Nautilus (`nautilus -q`)

## Manual installation

#### Install Dependencies

Fedora `sudo dnf install nautilus-python python3-gobject`

Ubuntu `sudo apt install python3-nautilus python3-gi`

Arch `sudo pacman -S python-nautilus python-gobject`

#### Download & Install the Extension

1. `git clone https://github.com/chr314/nautilus-copy-path.git`

2. `cd nautilus-copy-path`

3. `make install`

4. Restart the Nautilus (`nautilus -q`) if not seeing the options.

## Uninstallation

1. `cd path/to/nautilus-copy-path`
   
2. `make uninstall`
   
3. Restart the Nautilus (`nautilus -q`) if still seeing the options after uninstall.

## Configuration
configuration file: [config.json](config.json)

example:
```json
{
  "items": {
    "path": true,
    "uri": true,
    "name": true
  },
  "selections": {
    "clipboard": true,
    "primary": true
  },
  "language": "auto",
  "separator": ", "
}
```


## Currently supported languages 
- Chinese
- Danish
- English
- French
- German
- Greek
- Italian
- Japanese
- Norwegian
- Polish
- Portuguese
- Romanian
- Russian
- Spanish
- Swedish
- Turkish

#### Add new translations

Translations files are in `translations` directory

example: [English Translation](translations/en.json)

1. Copy the english translation file (`en.json`), the new file name must be the new language code (e.g. `es.json`)

2. Translate the values in the new file

3. Add information in the README in the section *Currently supported languages* about new language 

3. Create Pull Request with the new translation
