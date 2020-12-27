.DEFAULT_GOAL := all

all:
	@echo "Start build and runnig;"
	docker build -t python_volume_app .
	docker run python_volume_app
#	docker run -v "$(pwd)"/app_vol:/usr/src/app/app_vol python_volume_app

build:
	@echo "Start build;"
	docker build -t python_volume_app .

run:
	@echo "Start running;"
	docker run python_volume_app
#	docker run -v "$(pwd)"/app_vol:/usr/src/app/app_vol python_volume_app