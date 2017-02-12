all: dependencies enviroment


dependencies:
	apt-get update
	apt-get install -y python3 python3-pip python3-venv


enviroment:
	( \
		python3 -m venv venv                            ; \
		. venv/bin/activate                             ; \
		pip install --upgrade pip                       ; \
		pip install --upgrade -r requirements.txt       ; \
	)


clean:
	rm -rf ./venv


fresh: clean
	git reset --hard
	git clean -fd
