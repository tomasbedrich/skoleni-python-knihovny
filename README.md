# Nejlepší knihovny pro Python 3 - materiály pro výuku

Volně navazuje na školení [Základy Pythonu 3](https://github.com/tomasbedrich/skoleni-python).

## Instalace

Potřebný SW je:

- Python >= 3.5 (ověříte napsáním `python3 --version`)
- PIP >= 8 (ověříte napsáním `pip3 --version`)
- Virtualenv (ověříte napsáním `python3 -m venv`)

### Linux (Ubuntu, Debian a podobné)

```
sudo apt-get install -y git build-essential
git clone https://github.com/tomasbedrich/skoleni-python-knihovny
cd skoleni-python-knihovny
sudo make dependencies
make enviroment
source venv/bin/activate
```

### Windows

Stáhněte si instalátor Pythonu [z oficiálních stránek](https://www.python.org/downloads/). **Při instalaci nezapomeňte zaškrtnout *Add Python to PATH*.**

![Instalační obrazovka s volbou "Add Python to PATH"](http://loadbalancerblog.com/sites/default/files/images/image003.jpg)

- Stáhněte si tento repozitář kliknutím na zelené tlačítko *Clone or download > Download ZIP* v hlavičce této stránky, archiv rozbalte.
- Otevřete Příkazový řádek (*Start > vyhledat: cmd*)
- Opakováním příkazů `cd slozka` vyhledejte složku se staženými materiály.

Pak zadejte příkazy:

```
python3 -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
```

### OS X

Je dobré mít nainstalované Apple Developer Command Line Tools.

```
xcode-select --install
```

Python pak lze nainstalovat buď podobně jako pro Windows, pomocí oficiálního instalátoru, nebo lze použít balíčkovací manažer [Homebrew](http://brew.sh/) nebo [MacPorts](https://www.macports.org/).

Instalace pomocí MacPorts:

```
sudo port selfupdate
sudo port install -y git python35 py35-pip py35-virtualenv
sudo port select --set python3 python35
git clone https://github.com/tomasbedrich/skoleni-python-knihovny
cd skoleni-python-knihovny
make enviroment
source venv/bin/activate
```
