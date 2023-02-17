<?php

$mySal = 40000;

$strg = 'The given Salary is $mySal';

echo $strg. "\n";

eval("\$strg = \"$strg\";");

echo $strg. "\n";

?>