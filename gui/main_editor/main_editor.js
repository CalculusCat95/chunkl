var project = null;

function loadProject(file) {
    project = file;
}

function save() {
    if (project==null) {
        getSavePath();
    }
    fileWrite(project);
}