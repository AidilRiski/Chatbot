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

                if (isset($_POST['conversationCache']) && !isset($_POST['solveMethod'])){
                    $toWrite = 'Botty: Tolong pilih metode penyelesaian! UwU<br>';
                    echo $toWrite;
                    $conversationCache = $conversationCache.$toWrite;
                }else if (isset($_POST['solveMethod']) && isset($_POST['query'])){
                    $cleanQuery = '';
                    $splitQuery = str_split($_POST['query']);
                    $isSpace = true;
                    foreach ($splitQuery as $char){
                        if ($isSpace){
                            if ($char != ' '){
                                $isSpace = false;
                                $cleanQuery = $cleanQuery.$char;
                            }
                        }else {
                            if ($char == ' '){
                                $isSpace = true;
                            }
                            $cleanQuery = $cleanQuery.$char;
                        }
                    }
                    if ($cleanQuery != ''){
                        $run_command = 'python3 src/main.py '.$_POST['solveMethod'].' '.$cleanQuery.' 2>&1';
                        exec($run_command).'<br>';

                        $result_file = fopen('./data/result.txt', 'r');
                        $result_questions_array = array();
                        $result_answers_array = array();

                        $answerCount = 0;
                        while (!feof($result_file)){
                            $currentLine = fgets($result_file);
                            if ($currentLine != ''){
                                array_push($result_questions_array, explode(',', $currentLine)[0]);
                                array_push($result_answers_array, explode(',', $currentLine)[1]);
                                $answerCount = $answerCount + 1;
                            }
                        }

                        $count = 0;
                        if ($answerCount > 0){
                            foreach ($result_questions_array as $question){
                                if ($answerCount == 1){
                                    //$toWrite = 'You: '.$question.'<br>'.'Botty: '.$result_answers_array[$count].'<br>';
                                    $toWrite = 'You: '.$cleanQuery.'<br>'.'Botty: '.$result_answers_array[$count].'<br>';
                                }
                                else if ($answerCount > 1){
                                    if ($count == 0){
                                        $toWrite = 'You: '.$cleanQuery.'<br>'.'Botty: Apakah maksud anda<ol><li>'.$question.'</li>';
                                    }else if ($count > 0 && $count < $answerCount - 1){
                                        $toWrite = '<li>'.$question.'</li>';
                                    }else if ($count == $answerCount - 1){
                                        $toWrite = '<li>'.$question.'</li></ol>';
                                    }
                                }
                                echo $toWrite;
                                $conversationCache = $conversationCache.$toWrite;
                                $count = $count + 1;
                            }
                        }else {
                            $toWrite = 'You: '.$cleanQuery.'<br>'.'Botty: Botty tidak mengerti XD<br>';
                            echo $toWrite;
                            $conversationCache = $conversationCache.$toWrite;
                        }
                    }else {
                        $toWrite = 'Botty: Tolong katakan sesuatu, Botty kesepian :(<br>';
                        echo $toWrite;
                        $conversationCache = $conversationCache.$toWrite;
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
            <div id='solveMethodArea'>
                <input type="radio" name="solveMethod" value="kmp">KMP<br>
                <input type="radio" name="solveMethod" value="boy">Boyer-Moore<br>
                <input type="radio" name="solveMethod" value="reg">Regular Expression<br>
            </div>
            <?php
                echo '<div id="hidden">
                    <input type="hidden" name="conversationCache" value="'.$conversationCache.'"
                </div>'
            ?>
        </form>
    </body>
</html>