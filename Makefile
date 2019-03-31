install:
	mkdir -p ~/.local/share/nautilus-python/extensions
	cp nautilus-copy-path.py ~/.local/share/nautilus-python/extensions

uninstall:
	rm ~/.local/share/nautilus-python/extensions/nautilus-copy-path.py
