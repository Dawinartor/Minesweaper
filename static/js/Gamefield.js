//TODO: Add developer faces instead of mines for the bombs
var gamefield = document.getElementById('gamefield');
var gameData; // data from back-end 


/**
 * Preprocessing the JSON gameobject to get all values to work with
 * 
 * @param {JSON} backEndJSON - Back-End JOSN object 
 */
function preProcessingGame() {
    // get game object from backend
    fetch('/startGame')
        .then(function(response) {
            return response.text() // takes Response text value
        })
        .then(function(text) {
            gameData = JSON.parse(text);
            console.log(gameData);
        })
        .then(function() {
            buildGamefield(gameData);
        })

}

//TODO: Add checking if gameobject arrived in correct form. -> Typescript

/**
 * Initinilize the visual part of the gamefield and adds to HTML document
 * 
 * @param {JSON} gameObject - Back-End JOSN object of the created game
 */
function buildGamefield(gameObject) {
    // create divs which represets Tiles
    var tileList = [];

    for (let i = 0; i < gameObject.Gamefield.fieldSize; i++) {

        // create the element
        let newTile = document.createElement('div');

        // define div classname as tile
        newTile.className = 'tile';

        // define all needed tile values in each tile
        newTile.setAttribute('tileIndex', String(gameObject.Gamefield.field[i].index));
        newTile.setAttribute('className', String(gameObject.Gamefield.field[i].className));
        newTile.setAttribute('coordinate-x', String(gameObject.Gamefield.field[i].x)); // is row
        newTile.setAttribute('coordinate-y', String(gameObject.Gamefield.field[i].y)); // is column

        // append it in HTML for game visualization
        gamefield.appendChild(newTile);

        // append to tileList 
        tileList.push(newTile);
    }

    // Get tile elements class from DOM
    const tiles = document.querySelectorAll('.tile');

    // Function to toggle popup (toggles .active) 
    const showTileCoordinates = (event) => {
        console.log( event.target );
    };

    // Assign event listener with callback to every button:
    tiles.forEach((tile) => {
        tile.addEventListener("click", showTileCoordinates);
    });

}

preProcessingGame();