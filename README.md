# Catservable 🐱🐱🐱
A simple API with amazing information about cats! 🐱

## Summary

1. [About this project](#about-this-project)
3. [API and endpoints](#api-and-endpoints)
4. [About the architecture](#about-the-architecture)
5. [How to run this project](#how-to-run-this-project)
6. [About logs and metrics](#about-logs-and-metrics)


## About this project
Catservable is a simple toy API to show how a Django application can be developed with logs and metrics in mind.

## API and endpoints
There are four(4) endpoints used to access the data:
* `/breeds` used to list all cat breeds
* `/breeds/{id}` used to list all information about one breed
* `/breeds/search/temper/{temper}` where you can search any breed using the temperament as parameter. ex: Intelligent, Energetic, ...
* `/breeds/search/origin/{origin}` used to search breeds using origin place as parameter. ex: Egypt, England, ...

Also, there's a Postman Collection that can be used to help with the requests.

## About the architecture
This project is a simple monolith with basic modeling around MVC(or MVT on Django terminology). We used `django-prometheus` to help with instrumentation. It exposes metrics about the view like number of requests, exceptions, latency, and others. 

Yet, we're logging the application directly from **Docker** using the **GELF** driver.

For database we used **PostgreSQL**, since it is a amazing relational and very well tested database.

Also, there are some jobs used to retrieve data from TheCatAPI. They could run using the **manage.py** command.

## How to run this project
The easiest way is using `docker-compose` to orquestrate all containers locally.
Just run
```bash
docker-compose up
```
on the root directory and the application will turn on.
You may wait a couple of seconds to let the stack startup. After that you can access:
* the API on `http://localhost:8000`
* the Grafana with metrics dashboard on `http://localhost:3000`
* the Prometheus time series database on `http://localhost:9090`
* and Graylog with log dashboars on `http://localhost:9000`

If it's the first time you're running the application, remember to run the jobs to ingest data from *TheCatAPI*.
1. `make retrieve_cat_breeds`
2. `make retrieve_cat_images`
3. `make retrieve_cats_with_hats`
4. `make retrieve_cats_with_sunglasses`

*PS: We're making use of sudo to call docker-compose, but this is the worst practice ever. Remember to configure your user to use docker without root permissions.*

## About logs and metrics

We're using Prometheus for instrumentation and metrics, Grafana for Dashboards and Graylog to log management. We will talk about each one below.
1. [Prometheus](#prometheus)
2. [Grafana](#grafana)
3. [Graylog](#graylog)

### Prometheus
Prometheus is a timeseries database system(TSDB) developed by the SoundCloud team to gather metrics and insights about running systems. Different from classic metrics systems like NewRelic or ElasticAPM, the application which will be metrified exposes a endpoint with all the information and Prometheus will scrape them. 

Our Prometheus installation will bootup with the stack and start to scrape out example application right away. 
You can access it on http://localhost:9090

### Grafana
Grafana is a visualization and analytics tool that can consume Prometheus information and generate visual indicators from it. We're already setup it so you just have to access http://localhost:3000 using *admin* as user and password. You will be asked to change your password. When entering, look for the `SRE Dashboard`, click and it will take you to the screen below:
![Grafana with the SRE Dashboard](https://github.com/decko/catservable/blob/main/grafana/grafana-sre-dashboard.png)

### Graylog
Graylog is one of the leaders solutions for log management. Sadly we couldn't find a way to configure it on the startup process. To help, we've created a Content Pack, with the input needed to consume the example application logs and a simple dashboard. To install it, go to **System -> Content Packs**. Upload the `django_logs.json` file that could be found on `graylog` folder. After that, you need to roll down the list, find the `SRE Log Dashboard`, and click on **Install** button.
After that, just go to `Search` page, click on "Play" button and watch the logs coming down.

