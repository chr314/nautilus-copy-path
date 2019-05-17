install:
	mkdir -p ~/.local/share/nautilus-python/extensions/nautilus-copy-path
	cp nautilus-copy-path.py ~/.local/share/nautilus-python/extensions
	cp nautilus_copy_path.py translation.py ~/.local/share/nautilus-python/extensions/nautilus-copy-path
	cp -R translations ~/.local/share/nautilus-python/extensions/nautilus-copy-path/translations

uninstall:
	rm ~/.local/share/nautilus-python/extensions/nautilus-copy-path.py
	rm -rf ~/.local/share/nautilus-python/extensions/nautilus-copy-path
