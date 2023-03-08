const electron = require("electron");
const path = require("path");
const { ipcMain } = require('electron');
const { spawn } = require('child_process');

const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

let mainWindow;
let loc = []
let title = []
let desc = []
let pathFile = ''
let mapLink = ''

function createWindow() {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: { nodeIntegration: true, contextIsolation: false },
  });
  // and load the index.html of the app.
  console.log(__dirname);
  mainWindow.loadFile(path.join(__dirname, "../build/index.html"));
}

ipcMain.on('entry-desc', (event, variableData) => {
  desc = variableData
  console.log(desc)
});
ipcMain.on('entry-loc', (event, variableData) => {
  loc = variableData
  console.log(loc)
});
ipcMain.on('entry-title', (event, variableData) => {
  title = variableData
  console.log(title)
});
ipcMain.on('file-finder', (event, selectedFile) => {
  pathFile = selectedFile
});
ipcMain.on('entry-map', (event, data) => {
  mapLink = data
});

ipcMain.on('run', () => {
  console.log(mapLink, pathFile)
  // try{
  var python = spawn("python", [
    "./manipulaExcel.py",
    pathFile,
    'https://www.google.com/maps/d/u/0/edit?mid=19Af8BUv6WDvFGncBjN45gxDzWUKGeKI'
  ]);
  // }catch(e){
  //   console.log(e)
  // }
  // python.stdout.on("data", function (data) {
  //   // Do some process here
  // });

  // python.stderr.on("data", (data) => {
  //   console.error(`stderr: ${data}`);
  //   console.log(`stderr: ${data}`);
  // });

  // python.on("close", (code) => {
  //   console.log(`child process exited with code ${code}`);
  // });
})

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on("ready", createWindow);