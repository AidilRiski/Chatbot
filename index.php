<!DOCTYPE html>
<html>
    <head>
        <title>Chatbot</title>
    </head>
    <body>
        <h1>Welcome</h1>
        <?php 
            echo 'Chatbot';
            echo '<br>';
            $test_python = exec('python test.py');
            echo $test_python;
            echo '<br>';
        ?>
    </body>
</html>