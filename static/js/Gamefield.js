var gamefield = document.getElementById('gamefield');
//TODO: Add test backEndJSON

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
    var tileList = [256]; //gameObject.__fieldSize = 256

    for (let i = 0; i < tileList.length; i++) {

        var newTile = document.createElement('div');
        newTile.className = 'tile';
        gamefield.appendChild(newTile);

    }

    console.log(tileList[0]);

}

buildGamefield(null);