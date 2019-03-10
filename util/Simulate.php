<?php
//key is used to timecode the graph pictures
    $test = exec("Simulation.py " . $_GET['key']);
    echo($test);
?>