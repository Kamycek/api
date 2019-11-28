JavaScript to język programowania, który będziemy używać do wykonywania skryptów na stronie internetowej po stronie klienta.

Javascript możemy dołączyć:
W pliku *.html pomiędzy tagami `<script></script>`

######index.html
```html
<!doctype html>
<html>
    <head>
        <title>Document</title>
        <script>//Kod javascript</script>
    </head>
    <body> 
    </body>
</html>
```
W zewnętrznym pliku dołączonym do pliku *.html za pomocą `<script src="myscripts.js"></script>`

######index.html
```html
<!doctype html>
<html>
    <head>
        <title>Document</title>
        <script src="script.js"></script> <!--Dołączenie zewnętrznego pliku javascrip-->
    </head>
    <body> 
    </body>
</html>
```