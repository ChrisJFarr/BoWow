<?php

 $data_header = "Request Data";
 $key         = trim($_POST['key']);
 $value       = trim($_POST['value']);
 $file        = "request.json";

 $json = json_decode(file_get_contents($file), true);

 $json[$data_header] = array("key" => $key, "value" => $value);

 file_put_contents($file, json_encode($json, JSON_PRETTY_PRINT));
 
 echo "Success";

?>