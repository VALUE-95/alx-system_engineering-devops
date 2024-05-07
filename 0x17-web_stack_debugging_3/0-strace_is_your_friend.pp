exec { 'fix_apache_error':
  command     => '/usr/sbin/service apache2 restart',
  refreshonly => true,
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix_apache_error'],
}
