FROM handsonsecurity/seed-server:apache-php

ARG WWWDir=/var/www/SQL_Injection

COPY Code $WWWDir
COPY sql_injection.conf  /etc/apache2/sites-available
RUN rm /etc/apache2/sites-available/000-default.conf
RUN  a2ensite sql_injection.conf 



