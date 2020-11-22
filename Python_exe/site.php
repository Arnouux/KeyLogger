<html>
<head>
</head>
<body>
hello world
</body>
</html>
<?php
$dir = 'dist_zip.zip';
echo " hello world 2";
if (file_exists($dir)) {
	ob_clean();
	ob_end_flush();
    header("Content-type: application/zip"); 
	header("Content-Disposition: attachment; filename=/kl.zip");
	header("Content-length: " . filesize($dir));
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: no-cache');
    readfile($dir);

    exit;
}
?>