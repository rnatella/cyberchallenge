<!DOCTYPE html>
<html>
<body>

<a href="<?php echo $_SERVER['PHP_SELF'];?>?name=CIAO">Test $_GET</a>

<br><br>

<?php
if ($_SERVER["REQUEST_METHOD"] == "GET") {
  
  // collect value of input field

  if (isset($_GET['name'])) {
    echo $_GET['name'];
  }
}
?>

</body>
</html>