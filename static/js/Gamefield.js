//TODO: Add developer faces instead of mines for the bombs
var gamefield = document.getElementById('gamefield');
var gameData; // data from back-end 
const socket = io();

// this part recieves the modified json
socket.on("newjson", (data) => {
    gameData = JSON.parse(data);
    blankDelete(gameData)
  });


socket.on("initialize", (data) => {
    gameData = JSON.parse(data);
    blankDelete(gameData); 
  });

socket.on("final", (data) => {
    if (data == "Bomb") {
        location.reload();
    }
    if (data == "YouWin") {
        $('#gamefield').empty();
        $( "p" ).add( "<span>You Win</span>" ).appendTo('#gamefield');
    }

  });




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

        socket.emit('click', tileJSON);
    
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



function blankDelete(gameObject){
    $('#gamefield').empty();

    for (let i = 0; i < gameObject.Gamefield.fieldSize; i++) {
        let newTile = document.createElement('div');
        let tileP = document.createElement('p');
        // newTile.appendChild(tileP)

        tileP.innerHTML = "0"
        newTile.innerHTML = "&nbsp&nbsp"

        tileP.style.visibility = 'hidden'
        // newTile.style.visibility = 'hidden'
        
        if (gameObject.Gamefield.field[i].isLightUp == true) {
            newTile.className = 'blank';
            
            if (gameObject.Gamefield.field[i].number > 0 ){
                tileP.style.visibility = 'visible'
                newTile.style.visibility = 'visible'
                tileP.innerHTML = String(gameObject.Gamefield.field[i].number);
                newTile.innerHTML = String(gameObject.Gamefield.field[i].number);
            }
        }          
        else{
            newTile.className = 'tile';
        }
        newTile.setAttribute('tileIndex', String(gameObject.Gamefield.field[i].index));
        newTile.setAttribute('coordinate-x', String(gameObject.Gamefield.field[i].x)); // is row
        newTile.setAttribute('coordinate-y', String(gameObject.Gamefield.field[i].y)); // is column
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
        socket.emit('click', tileJSON);
    
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
