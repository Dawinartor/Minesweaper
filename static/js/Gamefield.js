var gamefield = document.getElementById('gamefield');
//TODO: Add test backEndJSON

//TODO: Add developer faces instead of mines for the bombs

/**
 * Preprocessing the JSON gameobject to get all values to work with
 * 
 * @param {JSON} backEndJSON - Back-End JOSN object 
 */
function preProcessingGameobject(backEndJSON) {

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

    for (let i = 0; i < 256 ; i++) { //* gameObject.__fieldSize = 256
        let newTile = document.createElement('div');
        // define div classname as tile
        newTile.className = 'tile';

        // append it in HTML for game visualization
        gamefield.appendChild(newTile);
        // append to tileList 
        tileList.push(newTile);
    }

    // Get tile elements from DOM
    const tiles = document.querySelectorAll('.tile');

    // Function to toggle popup (toggles .active) 
    const clickedTileCoordinates = () => {
        console.log( "xyz" );
        // tiles.classList.toggle("active"); 
    };

    // Assign event listener with callback to every button:
    tiles.forEach((tile) => {
        tile.addEventListener("click", clickedTileCoordinates);
    });
}

buildGamefield(null);