<?php
	//get the movie part that was sent by the client
	extract($_GET);
	$file=fopen("http://127.0.0.1:5000/static/text/SRN.txt","r");
	$SRNarray=array();
	//read the file contents, one line at a time and see
	//if we have an initial string match. if so, pick up
	//that line and add it to an array. We can send it
	//as a JSON to the client.
	while ($line=fgets($file))  {
		$SRN=trim($line);
		//strncasecmp(needle,haystack,count)
		if(strncasecmp($SRNpart, $SRN, strlen($SRNpart))==0){
			$SRNarray[]=$SRN;
		}
	}
	echo json_encode($SRNarray);

?>