<?php
include('antesh.php');

if($argv[1] != ""){
	$ticker = $argv[1];
	echo $ticker . "\n";
	
	echo "pystocklib...\n";
	$pystocklib_data = new Antesh('C:\xampp\htdocs\deepforcasting\pystocklib\auto.py', array($ticker));
	echo "pystocklib Finished!\n";

	echo "StockNN...\n";
	$StockNN_data = new Antesh('C:\xampp\htdocs\deepforcasting\StockNN\auto.py', array($ticker,'--retrain'));
	echo "StockNN Finished!\n";
}
?>