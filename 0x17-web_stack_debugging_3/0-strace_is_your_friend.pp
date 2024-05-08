# Fix 500 error when a GET HTTP method is requested to Apache web server.
file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => file('/var/www/html/wp-settings.php').content.gsub('phpp', 'php'),
}
