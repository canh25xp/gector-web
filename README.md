# Gec-web: Grammatical Error Correction Web Application

This project is using [Bootstrap](https://getbootstrap.com) version [5.2.3](https://getbootstrap.com/docs/5.2/getting-started/download/).
Download it with

```
curl -LO https://github.com/twbs/bootstrap/releases/download/v5.2.3/bootstrap-5.2.3-dist.zip
7z x bootstrap-5.2.3-dist.zip -ostatic
```

Tested with python 3.7, 3.8 and 3.9

## Installation

1. Clone the repository.

```sh
git clone https://github.com/canh25xp/gector-web --depth 1
```

2. Set up a virtual environment (>=Python 3.7).

```sh
# with conda
conda create -n gector-web python=3.8
conda activate gector-web
# with venv
python3 -m venv .venv
. .venv/bin/activate
```

3. Install dependencies and resources

```sh
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python # start python interactive shell and type following:
> import nltk
> nltk.download("punkt_tab")
> exit()
```

4. Modify the `application.secret_key` in `app.wsgi`.

5. Run it with `python app.py`

6. Optionally, for installation of MEMT, clone the MEMT repository:

```sh
git clone https://github.com/kpu/MEMT.git combinations/memt/memt/
```

   Then, follow the installation steps in `combinations/memt/memt/install`.
   ESC can run without additional installation.

7. Configure your web server (Apache, NGINX, etc...) to load and serve gec-web.
   I serve gec-web with mod_wsgi==4.9.4 and Apache 2.4.52. If you want to use mod_wsgi, follow the installation steps in <https://pypi.org/project/mod-wsgi/>

## GEC model API

The API information for all base models are defined in `config.py`
