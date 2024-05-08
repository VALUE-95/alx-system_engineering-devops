# Fix 500 error when a GET HTTP method is requested to Apache web server.
$fix='/var/www/html/wp-settings.php'
file { $fix:
  ensure => file,
}
exec {'fix typo in settings config':
  path    => ['/bin/', '/usr/bin/', '/usr/sbin/'],
  command => "sed -i s/phpp/php/g ${fix}",
  require => File[$fix],
}
