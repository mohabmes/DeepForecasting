<?php
//Links PHP with Python
class Linker{
	private
		//Configs
		$_cmd_src = 'c:\WINDOWS\system32\cmd.exe', //OR 'cmd'
		$_conda_act = 'C:\Users\mmes\Anaconda3\Scripts\activate.bat',         //Path to Anaconda activate.bat file
		$_env_name = 'tensorflow',	                                        	//environment name
		$_python = 'C:\Users\mmes\Anaconda3\envs\tensorflow\python.exe',		//Python version (in use!)

		$_env_activate_cmd = '',        //environment activate cmd
		$_file_cmd = '',                //run python file cmd
		$_py_file = '',
		$_argv = array();

	function __construct($file_path, $argv = NULL){
		$this->check_configs();

		if(isset($argv)){
			$this->_argv = $argv;
		}

		if(!empty($file_path)){
			$this->env_activate_cmd();
			$this->exec_py($file_path);
			$this->run_py_file_cmd();
			$this->run();
		}
	}

	function env_activate_cmd(){
		$this->_env_activate_cmd = "$this->_cmd_src /c $this->_conda_act activate $this->_env_name";
	}

	function exec_py($file_path){
		$this->_py_file = $file_path;
	}

	function run_py_file_cmd(){
		$this->_file_cmd = "$this->_python $this->_py_file" . $this->prepare_argv();
	}
	function run(){
		system("$this->_env_activate_cmd && $this->_file_cmd", $out);
		echo $out;
	}

	function check_configs(){
		if(	empty($this->_cmd_src) || empty($this->_conda_act)
			|| empty($this->_env_name) || empty($this->_python)
		){
			exit();
		}
	}

	function prepare_argv(){
		$argv = ' ';
		if(count($this->_argv)>0){
			foreach($this->_argv as $arg){
				$argv .= $arg . ' ';
			}
		}
		return $argv;
	}
}
?>