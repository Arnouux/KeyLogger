<?php

echo $_POST["data"];
file_put_contents("uploads/output.txt", "\n", $flags=FILE_APPEND);
file_put_contents("uploads/output.txt", $_POST["data"], $flags=FILE_APPEND);

/*
if (isset($_FILES["file"]["name"])) {

    $name = $_FILES["file"]["name"];
    $tmp_name = $_FILES['file']['tmp_name'];
    $error = $_FILES['file']['error'];

    if (!empty($name)) {
        $location = 'uploads/';

        if  (move_uploaded_file($tmp_name, $location.$name.".txt")){
            echo 'Uploaded';
        }
        else {
            echo "Error";
        }

    } else {
        echo 'please choose a file';
    }
}
else {
    echo "Error isset";
}
*/
?>