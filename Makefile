install:
	mkdir -p ~/.local/share/nautilus-python/extensions/nautilus-copy-path
	cp nautilus-copy-path.py ~/.local/share/nautilus-python/extensions
	cp nautilus_copy_path.py translation.py config.json ~/.local/share/nautilus-python/extensions/nautilus-copy-path
	cp -rf translations ~/.local/share/nautilus-python/extensions/nautilus-copy-path
	nautilus -q

uninstall:
	rm ~/.local/share/nautilus-python/extensions/nautilus-copy-path.py
	rm -rf ~/.local/share/nautilus-python/extensions/nautilus-copy-path
	nautilus -q
