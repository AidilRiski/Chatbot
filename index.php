<!DOCTYPE html>
<html>
    <head>
        <title>Chatbot</title>
    </head>
    <body>
        <h1>Welcome</h1>
        <form action="index.php" method="get">
            <input type="text" name="query"><br>
            <input type="submit" value="Ask!"><br>
        </form>
        <?php 
            echo 'Chatbot';
            echo '<br>';
            if (isset($_GET['query'])){
                $run_command = 'python src/main.py '.$_GET['query'];
                echo exec($run_command);

                $result_file = fopen('./data/result.txt', 'r');
                $result_questions_array = array();
                $result_answers_array = array();

                while (!feof($result_file)){
                    $currentLine = fgets($result_file);
                    array_push($result_questions_array, explode(',', $currentLine)[0]);
                    array_push($result_answers_array, explode(',', $currentLine)[1]);
                }

                $count = 0;
                foreach ($result_questions_array as $question){
                    echo $question.'<br>';
                    echo $result_answers_array[$count].'<br>';
                    $count = $count + 1;
                }
            }
        ?>
    </body>
</html>