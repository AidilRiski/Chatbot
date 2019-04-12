<!DOCTYPE html>
<html>
    <head>
        <title>Chatbot</title>
    </head>
    <body>
        <h1>Welcome</h1>
        <?php 
            echo 'Chatbot';
            $test_python = exec('test.py');
            echo '$test_python';
        ?>
    </body>
</html>