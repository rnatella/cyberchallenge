<!DOCTYPE html>
<html>
<body>

<h1>Welcome to my home page!</h1>

<?php 
    include 'noFileExists.php';

    echo "<p style='color:red'>";
    echo "I have a $color $car.";
    echo "</p>";
?>



<?php 
    require 'noFileExists.php';

    echo "<p style='color:blue'>";
    echo "I have a $color $car.";   // This will not be executed
    echo "</p>";
?>


</body>
</html>
