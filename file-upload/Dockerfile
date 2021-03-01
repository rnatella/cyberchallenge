FROM php:7.0-apache

COPY DVFU/ /var/www/html/
COPY config/php.ini /usr/local/etc/php/ 
COPY config/docker-php.conf /etc/apache2/conf-enabled/

RUN chown -R www-data.www-data /var/www/html/vulnerabilities/
