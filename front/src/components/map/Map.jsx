import React from 'react'
import { ipcRenderer } from 'electron';

export default function Map (){
    function setNewEntry() {
        ipcRenderer.send(`entry-map`, document.getElementById('map').value);
    }
    return (
        <div className="entry mb-2">
                <div className="input-group">
                    <input type="text" id='map' 
                        className="form-control" placeholder='Link do map' />
                    <button type="button" className="btn btn-primary"
                        onClick={e => setNewEntry(e)}>+</button>
                </div>
            </div>
    )
}