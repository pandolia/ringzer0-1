<?php
    $url     = 'https://ringzer0team.com/challenges/48';
    $ch      = curl_init($url);
    $options = array(CURLOPT_CUSTOMREQUEST => 'TOTO');
    curl_setopt($ch, CURLOPT_COOKIE, 'PHPSESSID=o4m5bk4cs51k1673febs3qikk1');
    curl_setopt_array($ch, $options);

    $res = curl_exec($ch);
    echo $res;
?>
