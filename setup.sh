#!/bin/bash

git clone https://github.com/sudoskys/Tool-Asoul-Music
cd Tool-Asoul-Music
echo '============NOTICE================='
echo 'you need edit the config.yaml!'
echo '==================================='
cat config.yaml
echo '==================================='

read -r -p "Install package from requirements.txt? [Y/n] " input

case $input in
    [yY][eE][sS]|[yY])
		python3 -m pip install -r requirements.txt
		;;

    [nN][oO]|[nN])
		exit 1
        ;;
    *)
		echo "Invalid input..."
		exit 1
		;;
esac
