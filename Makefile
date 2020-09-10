 
# Terslation - Terminal Translator
# git clone https://github.com/denstiny/Terslation.git

install:
	cp -f SpeekABread.sh /bin/SpeekABread
	cp -f SpeekABreadc.sh /bin/Spread 
	pip install baidu_aip
	pip install pyaudio
	pip install wave
	pip install palysound
	chmod +x /bin/SpeekABread
	mkdir /usr/local/src/seek
	chmod 777 /usr/local/src/seek
	cp -f * /usr/local/src/seek/
	mkdir /usr/local/src/seek/File_shell
	@echo "Install successful."
init:
	ln -s /usr/local/src/seek/File_shell ~/.config/SpeekABread
	sudo chmod 775 ~/.config/SpeekABread
uninstall:
	rm /usr/bin/SpeekABread
	rm /usr/bin/Spread
	rm -r /usr/local/src/seek
	@echo "Uninstall successful."
