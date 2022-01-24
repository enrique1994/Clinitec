<?php
$dbuser = 'root';
$dbpass = '';
$dbname = 'celulares';
$con = mysqli_connect("localhost",$dbuser,$dbpass,$dbname);


	define('DB_HOST', 'localhost');
	define('DB_USER', $dbuser);
	define('DB_PASS', $dbpass);
	define('DB_NAME', $dbname);
	define('DB_CHARSET', 'utf8');


// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }





try{
	$base_de_datos = new PDO('mysql:host=localhost;dbname=' . $dbname, $dbuser, $dbpass);
	 $base_de_datos->query("set names utf8;");
    $base_de_datos->setAttribute(PDO::ATTR_EMULATE_PREPARES, FALSE);
    $base_de_datos->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $base_de_datos->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_OBJ);
}catch(Exception $e){
	echo "Ocurrió algo con la base de datos: " . $e->getMessage();
}
?>