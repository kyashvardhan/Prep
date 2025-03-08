<?php
require 'vendor/autoload.php';
use TCPDF;

$pdf = new TCPDF();
$pdf->AddPage();
$pdf->SetFont('Helvetica', '', 12);
$pdf->Write(0, 'Hello, PDF World!');
$pdf->Output('document.pdf', 'F');
?>
