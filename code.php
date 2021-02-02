<?php

$code = $_POST['code'];

if ($code == "0310") {
    $srt = "";
    echo(str_replace('{% block contenu %}{% endblock %}', str_replace('{% endblock contenu %}', '', str_replace('{% extends "layout.html" %}{% block contenu %}', '', file_get_contents('Hydrogene.html')), str_replace('{% if titre %}<title>O.D.A.A.M.E. - {{ titre }}</title>{% else %}<title>O.D.A.A.M.E.</title>{% endif %}', "<title>O.D.A.A.M.E.</title>", file_get_contents('layout.html'))));
    echo($srt);
}
?>