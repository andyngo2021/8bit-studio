let val;

window.onload = function()
{
    console.log("hello world!");
}

window.onunload = function()
{
    eel.closeApp();
    window.close();
}

window.oncontextmenu = function(event) {
    // block right-click / context-menu
    event.preventDefault();
    event.stopPropagation();
    return false;
};

function go()
{
    eel.getFile()(filename_resp);
    
}
let f = "";
function filename_resp(filename)
{
    console.log(filename);
    document.getElementById("main-display").src = filename;
    f = filename;
}

function PIXELATE()
{
    val = document.getElementById("pixelator-slider").value;
    sendValToPy(val);
    // console.log("hi!");
}

eel.expose(sendValToPy);
function sendValToPy()
{
    console.log("hi");
    eel.acceptValFromJS(val);
    // document.getElementById("main-display").src = f;
    // return 5;
}