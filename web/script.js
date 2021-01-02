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

function filename_resp(filename)
{
    console.log(filename);
    document.getElementById("main-display").src = filename;
}