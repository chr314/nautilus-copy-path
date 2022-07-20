import os
import json
import shlex
from translation import Translation
from gi.repository import Nautilus, GObject, Gtk, Gdk
from gi import require_version

require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')


class NautilusCopyPath(Nautilus.MenuProvider, GObject.GObject, Nautilus.LocationWidgetProvider):

    def __init__(self):
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.clipboard_primary = Gtk.Clipboard.get(Gdk.SELECTION_PRIMARY)

        self.config = {
            "items": {
                "path": True,
                "uri": True,
                "name": True
            },
            "selections": {
                "clipboard": True,
                "primary": True
            },
            "shortcuts": {
                "path": "<Ctrl><Shift>C",
                "uri": "<Ctrl><Shift>U",
                "name": "<Ctrl><Shift>N"
            },
            "language": "auto",
            "separator": ", ",
            "escape_value_items": False,
            "escape_value": False
        }

        with open(os.path.join(os.path.dirname(__file__), "config.json")) as json_file:
            try:
                self.config.update(json.load(json_file))
                if self.config["language"]:
                    Translation.select_language(self.config["language"])
            except:
                pass

        self.accel_group = Gtk.AccelGroup()
        for key in self.config["shortcuts"]:
            try:
                keyval, modifier = Gtk.accelerator_parse(self.config["shortcuts"][key])
                self.accel_group.connect(keyval, modifier, Gtk.AccelFlags.VISIBLE,
                                         lambda *args, action=key: self._shortcuts_handler(action, *args))
            except:
                pass

        self.window = None

    def _shortcuts_handler(self, action, accel_group, acceleratable, keyval, modifier):
        items = self._get_selection()
        action_function = {'path': self._copy_paths, 'uri': self._copy_uris, 'name': self._copy_names}[action]
        if len(items) > 0 and action_function:
            action_function(None, items)
        return True

    def get_file_items(self, window, files):
        return self._create_menu_items(files, "File")

    def get_background_items(self, window, file):
        return self._create_menu_items([file], "Background")

    def get_widget(self, uri, window):
        if self.window:
            self.window.remove_accel_group(self.accel_group)
        window.add_accel_group(self.accel_group)
        self.window = window
        return None

    def _get_selection(self):
        focus = self.window.get_focus()
        items = []
        if not isinstance(focus, Gtk.TreeView) and focus.get_parent().get_name() == 'NautilusListView':
            return items

        focus.get_selection().selected_foreach(lambda tree, path, iter, uris: uris.append(tree[iter][0]), items)
        return items

    def _create_menu_items(self, files, group):
        plural = len(files) > 1
        config_items = self.config["items"]
        active_items = []

        if config_items["path"]:
            item_path = Nautilus.MenuItem(
                name="NautilusCopyPath::CopyPath" + group,
                label=Translation.t("copy_paths" if plural else "copy_path"),
            )
            item_path.connect("activate", self._copy_paths, files)
            active_items.append(item_path)

        if config_items["uri"]:
            item_uri = Nautilus.MenuItem(
                name="NautilusCopyPath::CopyUri" + group,
                label=Translation.t("copy_uris" if plural else "copy_uri"),
            )
            item_uri.connect("activate", self._copy_uris, files)
            active_items.append(item_uri)

        if config_items["name"]:
            item_name = Nautilus.MenuItem(
                name="NautilusCopyPath::CopyName" + group,
                label=Translation.t("copy_names" if plural else "copy_name"),
            )
            item_name.connect("activate", self._copy_names, files)
            active_items.append(item_name)

        return active_items

    def _copy_paths(self, menu, files):
        self._copy_value(list(map(lambda f: f.get_location().get_path(), files)))

    def _copy_uris(self, menu, files):
        self._copy_value(list(map(lambda f: f.get_uri(), files)))

    def _copy_names(self, menu, files):
        self._copy_value(list(map(lambda x: os.path.basename(x.get_location().get_path()), files)))

    def _copy_value(self, value):
        if len(value) > 0:
            if self.config["escape_value_items"]:
                value = list(map(lambda x: shlex.quote(x), value))

            new_value = self.config["separator"].join(value)

            if self.config["escape_value"]:
                new_value = shlex.quote(new_value)

            if self.config["selections"]["clipboard"]:
                self.clipboard.set_text(new_value, -1)
            if self.config["selections"]["primary"]:
                self.clipboard_primary.set_text(new_value, -1)
