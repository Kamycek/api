# Deklaracja i inicjalizacja

Zmienna w programowaniu służy do przechowywania wartości.
Na przechowywanych wartościach będziemy mogli wykonywać operacje.

Inicjalizacja to przypisanie wartości do zmienenej.

Zmienną deklarujemy i inicjalizujemy w następujący sposób:
 `let nazwa = wartość;`

 np. `let wiek = 5;`

W JavaScripcie zmienną deklarujemy za pomocą słowa kluczowego `let` nie podajemy typu danych,
jest on automatycznie dostosowywany do wartości.

Jeżeli chcemy by zmienna była ciągiem znaków (typu String) należy jej wartość zapisać w `""` lub `''`.
Wartości typu Number nie należy umiesczać w `""` ponienaważ uniemożliwia to wykonywanie na niej operacji arytmetycznych.

# Zmiana watości i const

Wartość zmiennej zadeklarowanej za pomocą `let` możemy nadpisać w dowolnym momencie.

```js
let x = 2; // zmienna x ma wartość 2
x = 5; // zmiana wartości zmiennej x na 5
```

Zmienną możemy zadeklarować za pomocą `const`. Taką zmienną nazywamy stałą. Wartości takiej stałej nie możemy nadpisać.

```js
const pi = 3.1; // stała x ma wartość 2
x = 3.14; // BŁĄD spowodowany próbą zmiany wartości stałej
```

# Typy proste

| typ | przykład | opis |
|-----|----------|------|
|number|`3.14`|Wartość liczbowa|
|string|`"tekst"`|Ciąg znaków|
|boolean|`true`|Wartość logiczna true lub false|
|symbol|`Symbol('opis')`|Przyjmuje unikatową wartość niezależnie od opisu|
|null|`null`|Brak wartości nigdy nie ustawiany przez JS|
|undefined|`undefined`|Brak wartości ustawiany przez JS|

# Inne sposoby deklarowania zmiennych
Dawnie
