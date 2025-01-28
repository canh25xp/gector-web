# Gec-web: A Lightweight Language Error Correction System

This project is using [Bootstrap](https://getbootstrap.com) version [5.2.3](https://getbootstrap.com/docs/5.2/getting-started/download/).
Download it with 
```
curl -LO https://github.com/twbs/bootstrap/releases/download/v5.2.3/bootstrap-5.2.3-dist.zip
7z x bootstrap-5.2.3-dist.zip -ostatic
```

## Installation
1. Clone the repository.
2. Set up a virtual environment (>=Python 3.7).
3. Run `pip install -r requirements.txt`.
4. Run `python3 -m spacy download en_core_web_sm`
5. Modify the `application.secret_key` in `app.wsgi`.
6. Run `python app.py` in the root directory to verify your installation.
7. Optionally, for installation of MEMT, run `git clone https://github.com/kpu/MEMT.git combinations/memt/memt/` to clone the MEMT repository.
   Then, follow the installation steps in `combinations/memt/memt/install`. ESC can run without additional installation.
8. Configure your web server (Apache, NGINX, etc...) to load and serve gec-web.
   I serve gec-web with mod_wsgi==4.9.4 and Apache 2.4.52. If you want to use mod_wsgi, follow the installation steps in <https://pypi.org/project/mod-wsgi/>

## GEC model API

The API information for all base models are defined in `config.py`
