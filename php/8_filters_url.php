<!DOCTYPE html>
<html>
<body>

<?php
$url = "https://www.w3schools.com@@@";

// Remove all illegal characters from a url
// This filter allows all letters, digits and $-_.+!*'(),{}|\\^~[]`"><#%;/?:@&=
$url = filter_var($url, FILTER_SANITIZE_URL);

// Validate url
if (!filter_var($url, FILTER_VALIDATE_URL) === false) {
  echo("$url is a valid URL");
} else {
  echo("$url is not a valid URL");
}
?>

</body>
</html>
