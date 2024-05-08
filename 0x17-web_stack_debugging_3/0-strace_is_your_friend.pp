# Fix 500 error when a GET HTTP method is requested to Apache web server.

exec {'Fix wordpress site':
  command => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
