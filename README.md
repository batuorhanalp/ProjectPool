=====================
Karbonat Fikir Havuzu
=====================

This is a project where you can store your project ideas and categorize them on budget etc.

Installation
============

Install virtualenv if it's not installed before

    pip install virtualenv

Use following to set up the project

    virtualenv venv --distribute
    source venv/bin/activate
    pip install -r requirements/local.txt 

Running The Project
===================
  
Each time you start developing or running, make sure you run the following command:

    source venv/bin/activate

First time installation (and whenever you change anyhing in the models, also make sure that issue `cd project_pool` if you're not in the development folder):

    python manage.py syncdb

To run the project issue following commands (`cd project_pool` if you're not in the development folder):

    python manage.py runserver_plus

Visit `http://localhost:8000/` on your browser. You have run the project in development environment.

Deployment
==========

Bir django uygulamasini deploy etmek icin bircok yontem mevcut. Ben en kolay gordugum yontemi buraya yaziyorum:

	git clone https://github.com/batuorhanalp/ProjectPool.git
	cd ProjectPool

Bu noktada `project_pool/project_pool/settings/production.py` dosyasindan database bilgilerini girmek gerekiyor.

	virtualenv venv --distribute
    source venv/bin/activate
    pip install -r requirements/local.txt 

Django ayarlarini yapalim. `syncdb` sirasinda bir admin hesabi olusturalim (yonergeleri izleyin sadece).

	cd project_pool
	python manage.py syncdb
	python manage.py collectstatic

Test icin test sunucusunu calistiralim, hata vermemeli

	python manage.py runserver

Simdi django'yu fastcgi ile 8081 portunda calistiralim

	python manage.py runfcgi host=127.0.0.1 port=8081

Fastcgi'i nginx uzerinden 8283 portunda sunalim. Baska bir port numarasi secileblir ya da 80 portunda bir domain name'de calistirilabilir. Bu nginx configurasyonunu `nginx.conf` ya da `sites-enabled` icinde yeni bir dosya olarak yapablirsiniz. Apache kullanilmak isteniyorsa da buna benzer bir vhost konfigurasyonu yapilmalidir. 

	server {
	    listen 8283;
	    server_name example.com;
	    access_log /var/log/nginx/karbonat.access.log;
	    error_log /var/log/nginx/karbonat.error.log;

		# https://docs.djangoproject.com/en/dev/howto/static-files/#serving-static-files-in-production
	    location /static/ { # STATIC_URL
	        alias /home/USERNAME/ProjectPool/project_pool/project_pool/compiled_static_files/; # STATIC_ROOT
	            expires 30d;
	    }
	    
	    location / {
	        include fastcgi_params;
	        fastcgi_pass 127.0.0.1:8081;
	        fastcgi_split_path_info ^()(.*)$;
	    }
	}

`nginx`i yeniden baslatalim:

	sudo service nginx restart

`fastcgi`in calistigindan emin olalim. Asagidaki komut sonunda, calisan processler gorulmeli:

	ps ax | grep runfcgi
