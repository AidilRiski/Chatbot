<!DOCTYPE html>
<html>
    <head>
        <title>Chatbot</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div id="titleBar">
            <h1>Welcome to Botty!</h1>
        </div>
        <div id="textArea">
            <?php
                $conversationCache = '';

                if (!isset($_POST['conversationCache'])){
                    $conversationCache = 'Botty: Hello!<br>';
                }else {
                    $conversationCache = $_POST['conversationCache'];
                }
                echo $conversationCache;

                if (isset($_POST['query'])){
                    $run_command = 'python3 src/main.py reg'.$_POST['query'].' 2>&1';
                    exec($run_command);

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
                        $toWrite = 'You: '.$question.'<br>'.'Botty: '.$result_answers_array[$count].'<br>';
                        echo $toWrite;
                        $conversationCache = $conversationCache.$toWrite;
                        $count = $count + 1;
                    }
                }
            ?>
        </div>
        <form action="index.php" method="post">
            <div id='queryArea'>
                Question:
                <input type="text" name="query" id='queryBox'><br>
            </div>
            <div id='submitArea'>
                <input type="submit" value="Ask!"><br>
            </div>
            <?php
                echo '<div id="hidden">
                    <input type="hidden" name="conversationCache" value="'.$conversationCache.'"
                </div>'
            ?>
        </form>
    </body>
</html>