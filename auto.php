<?php
include('linker.php');

if($argv[1] != ""){
	$ticker = $argv[1];
	$op = '--retrain';

	if(!empty($argv[2])){
	    $op = $argv[2];
	}
	echo $ticker . "\n";
	
	echo "pystocklib...\n";
	// $pystocklib_data = new Linker('.\pystocklib\auto.py', array($ticker));

	echo "StockNN...\n";
	$StockNN_data = new Linker('.\StockNN\auto.py', array($ticker, $op));
}
?>