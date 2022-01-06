var gamefield = document.getElementById('gamefield');


/**
 * Initinilize the visual part of the gamefield and adds to HTML document
 * 
 * @param {JSON} backEndJSON - Back-End JOSN object of the created game
 */
function buildGamefield(backEndJSON) {
    // create divs which represets Tiles
    var allTiles = document.createElement('div');
    var testText = document.createTextNode('I am a TEST');

    allTiles.appendChild(testText);
    
    // allTiles.classList.add('Tile')
    gamefield.appendChild(allTiles);

}
