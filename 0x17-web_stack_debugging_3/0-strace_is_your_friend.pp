# Fix 500 error when a GET HTTP method is requested to Apache web server.

exec { 'fix_apache_error':
  command     => '/usr/sbin/service apache2 restart',
  refreshonly => true,
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix_apache_error'],
}
