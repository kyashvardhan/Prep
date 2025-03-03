<?php
require 'vendor/autoload.php';
use Dompdf\Dompdf;

$dompdf = new Dompdf();
$dompdf->loadHtml('<h1>Hello, PDF!</h1>');
$dompdf->render();
$dompdf->stream("document.pdf");
?>
