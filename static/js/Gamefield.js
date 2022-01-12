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
    // create divs which represets each Tile

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
    }


    // Function to log each click in console
    const logClickedTile = (event) => {
        // takes clicked tile in variable
        let clickedTile = event.target;
        
        //~ for debugging
    /*
        console.log( 
            clickedTile.getAttribute('tileIndex') + " /",
            clickedTile.getAttribute('className') + " /",
            clickedTile.getAttribute('coordinate-x') + " /",
            clickedTile.getAttribute('coordinate-y') 
        );
    */
    };

    // Generates JSON from data
    const createJSON = (valueX, valueY) => {
        let returnJSON = {"tile": {
            "x": valueX,
            "y": valueY
        }};
        return returnJSON;
    }

    // collects information of clicked tile 
    const getTileInformations = (event) => {
        // takes clicked tile in variable
        let clickedTile = event.target;
        
        let tileIndex = clickedTile.getAttribute('tileIndex');
        let className = clickedTile.getAttribute('className');
        let valueX = clickedTile.getAttribute('coordinate-x');
        let valueY = clickedTile.getAttribute('coordinate-y');

        // generates JSON with needed information
        return createJSON(valueX, valueY);
    }

    const sendClickedTile = (tileJSON) => {
        // TODO: Trough fetch() send to back-end
        //console.log(tileJSON.tile.x)
    }

    /**
     * 
     * @param {*} clickedTile 
     */
    const onClickTile = (clickedTile) => {

        // log in system (console.log) each time which was clicked
        logClickedTile(clickedTile);
        // collect clicked tile information & generate JSON
        let clickedTileJSON = getTileInformations(clickedTile);
        console.log(clickedTileJSON);
        // send collected json
        sendClickedTile(clickedTileJSON);

    }

    // Get tile elements class from DOM
    const tiles = document.querySelectorAll('.tile');

    // Assign event listener with callback to every button:
    tiles.forEach((tile) => {
        tile.addEventListener("click", onClickTile);
    });

}

preProcessingGame();