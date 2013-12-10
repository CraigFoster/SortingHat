<?php
error_reporting(E_ALL);
set_time_limit (1000000);
file_put_contents("input.txt", $_REQUEST['handleText']);
while(true){
	if( file_get_contents("output.txt")!=""){
$filed = file_get_contents("output.txt");
exec("cat /dev/null > /var/www/html/output.txt");
		header("Location: hpAnalyze.php?req=".$filed); 
		echo "ran";break;
	}
	else{
	echo "still";
		}

	sleep(10);
}?>