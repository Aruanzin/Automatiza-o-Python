import React, { useState } from 'react'
import { ipcRenderer } from 'electron';
import './Run.css'

export default function Entry(props) {
    
    function run() {
        ipcRenderer.send(`run`);
    }

    return (
        <button className='btn btn-danger' onClick={run} style={{width: '65vw'}}>Rodar</button>
    )
}