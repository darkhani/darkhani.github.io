<?php
//echo "coin data ver 0.00.001";
$url = "https://api.bithumb.com/public/ticker/XRP";
$port = 443;
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_PORT, $port);
curl_setopt($ch, CURLOPT_POSTFIELDS, $request);
$response = curl_exec($ch);
curl_close($ch);
echo $response;
// the content of 'data.txt' is now 123 and not 23!
?>

