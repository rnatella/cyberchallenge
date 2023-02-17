<!DOCTYPE html>
<html>
<body>

<?php 
    echo $_SERVER['PHP_SELF'];
    echo "<br>\n";

    echo $_SERVER['SERVER_NAME'];
    echo "<br>\n";

    echo $_SERVER['HTTP_HOST'];
    echo "<br>\n";

    echo $_SERVER['HTTP_REFERER'];
    echo "<br>\n";

    echo $_SERVER['HTTP_USER_AGENT'];
    echo "<br>\n";
    
    echo $_SERVER['SCRIPT_NAME'];
?>

</body>
</html>
