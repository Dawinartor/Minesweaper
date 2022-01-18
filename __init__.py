"""Minesweeper server-side game

Dieses script hat alle nötigen Funktionen um ein Client-Server Minesweeper Spiel aufzusetzen.

Die haupt Klasse ist Gamefield.

Um das Minesweeper Spiel zu starten wird ein Object der Klasse Gamefield benötigt. Damit stehen
alle nötigen Informationen zum Spiel zur verfügung und können mit Hilfe von Getter abgerufen werden.

Um mit einem Server zu komunizieren wird das Feld des Spiels mit Hilfe von JSON verschickt.

Um diese Bibliothek verwenden zu können müssen folgende Bibliotheken 
installiert sein:

    * numpy
    * json
    * itertools
    * random
    
Wird die Bibliothek importiert stehen folgende Funtionen zur verfügung:

    * placeBombs
    * placeZeros
    * addValue
    * isLightUpChanger
    * blankOpener
    * toJSON
    * getFieldSize
    * getBombLocationList
    * getField
"""