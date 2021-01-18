retrieve_cat_breeds:
	sudo docker-compose exec api poetry run ./manage.py retrieve_cat_breeds

retrieve_cat_images:
	sudo docker-compose exec api poetry run ./manage.py retrieve_cat_images

retrieve_cats_with_hats:
	sudo docker-compose exec api poetry run ./manage.py retrieve_cat_with_accessories --accessory hats

retrieve_cats_with_sunglasses:
	sudo docker-compose exec api poetry run ./manage.py retrieve_cat_with_accessories --accessory sunglasses
