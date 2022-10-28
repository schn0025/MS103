## mise en place des différents utilisateurs

création de l'utilisateur schn0025 ayant pour uid 33514, gid 100 et chemin /home/schn0025 schn0025
	sudo adduser --uid 33514 --gid 100 --home /home/schn0025 schn0025


création de l'utilisateur admin ayant pour uid 31205, gid 100 et chemin /home/administrateur admin
 
	sudo adduser --uid 31205 --gid 100 --home /home/administrateur admin

ajout de admin au group sudo
	sudo adduser admin sudo

## installation
	### python
 281  sudo apt install python3

	### yapf
 290  sudo apt install python3-yapf

	### isort
 293  sudo apt install python3-isort

	### bandit
 296  sudo apt install python3-bandit

	### flake8
 297  sudo apt install python3-flake8

	### mypy
 300  sudo apt install python3-mypy

	### pygame
 302  sudo apt install python3-pygame

	### unitest
 307  sudo apt install python3-unittest

	### git
 309  sudo apt install git

	### meld
 310  sudo apt install meld

	### sphinx
 311  sudo apt install python3-sphinx
