<!DOCTYPE html>
<html>
<body>

<?php

// Replace "Microsoft" with "W3Schools" in a string

$str = "Visit Microsoft!";
$pattern = "/microsoft/i";

echo preg_replace($pattern, "W3Schools", $str);

?>

</body>
</html>
