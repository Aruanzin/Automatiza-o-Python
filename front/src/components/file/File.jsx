import React from 'react'
import { ipcRenderer } from 'electron';

export default function Entry() {

    function findFile(event) {
        const selectedFile = event.target.files[0];
        console.log(selectedFile)
        ipcRenderer.send(`file-finder`, selectedFile.path);
    }

    return (  
        <input type="file" class="form-control" onChange={(e) =>findFile(e)} style={{height: '58px', }} placeholder="Recipient's username" id="file" />
    )
}