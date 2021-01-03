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
    eel.getDimensions()(pydim);
}
let img_dim = [];
function pydim(dim)
{
    document.getElementById("img-w").value = dim[0];
    document.getElementById("img-h").value = dim[1];
    img_dim.push(dim[0]); // w
    img_dim.push(dim[1]); // h
}

let f = "";
function filename_resp(filename)
{
    // console.log(filename);
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
    eel.acceptValFromJS(val);
    document.getElementById("main-display").src = f;
}

function applyChanges()
{
    let w = document.getElementById("img-w").value;
    let h = document.getElementById("img-h").value;
    eel.getJSDim(w, h);
    document.getElementById("main-display").src = f;
}

function onchangeW()
{
    let check = document.getElementById("cb").checked;

    if (check) 
    {
        let w = document.getElementById("img-w").value;
        if (isNumeric(w))
        {
            let ratio = w/img_dim[0];
            let h = document.getElementById("img-h");
            let new_h = img_dim[1]*ratio;
            h.value = Math.floor(new_h);
        }
    }
}

function onchangeH()
{
    let check = document.getElementById("cb").checked;
    if (check)
    {
        let h = document.getElementById("img-h").value;
        if (isNumeric(h))
        {
            let ratio = h/img_dim[1];
            let w = document.getElementById("img-w");
            let new_w = img_dim[0]*ratio;
            w.value = Math.floor(new_w);
        }
    }
}

function onchangeCB()
{
    let check = document.getElementById("cb").checked;
    if (check)
    {
        let h = document.getElementById("img-h").value;
        let w = document.getElementById("img-w").value;
        if (h > w) onchangeH();
        else onchangeW();
    }
}

function isNumeric(value)
{
    // regex!??! POG!?!?
    return /^-?\d+$/.test(value);
}

function saveimg()
{
    eel.saveFile();
}