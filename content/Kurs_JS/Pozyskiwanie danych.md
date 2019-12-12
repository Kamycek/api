# prompt()
Funkcja prompt wyświetla okno dialogowe z treścią podaną jako parametr oraz oczekuje na wprowadzenie przez użytkownika wartości która może być przypisana do zmiennej w następujący sposób:
```js
let x = prompt('Podaj wartość', '3');
```
Jako drugi parametr możemy podać domyślną wartość która wyświetli sie w oknie dialogowym.

Wczytana wartość zawsze jest typu `string`. Jeżeli chcemy wykonywać na niej operacje arytmetyczne musumi zmienić jej typ na `number`.