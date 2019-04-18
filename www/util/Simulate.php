<?php
//key is used to timecode the graph pictures
    $time = $_GET['time'];
    $size = $_GET['size'];
    $var = $_GET['var'];
    $nwLat = $_GET['nwLat'];
    $nwLng = $_GET['nwLng'];
    $seLat = $_GET['seLat'];
    $seLng = $_GET['seLng'];
    
    $cmd = "Simulation.py ". $time . " " . $size . " " . $var . " " . $nwLat . " " . $nwLng . " " . $seLat . " " . $seLng;

    $result = shell_exec($cmd);
    
    if($result == NULL){
        $result = "Simulation Failed";
    }
    
    echo($result);
?>