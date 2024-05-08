# Fix 500 error when a GET HTTP method is requested to Apache web server.

exec { 'service apache2 restart': }
service { 'apache2': ensure => running, require => Exec['service apache2 restart'], }
