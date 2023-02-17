<!DOCTYPE html>
<html>
<body>

<?php

// Do a case-insensitive count of the number of occurrences of "ain" in a string

$str = "The rain in SPAIN falls mainly on the plains.";
$pattern = "/ain/i";

echo preg_match_all($pattern, $str);

?>

</body>
</html>
