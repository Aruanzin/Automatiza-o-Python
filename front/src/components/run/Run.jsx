import React, { useEffect, useState } from 'react'
import { ipcRenderer } from 'electron';
import './Run.css'

export default function Run() {

    function run() {
        ipcRenderer.send(`run`);
        document.getElementById('loading').style.display = 'block'
        document.getElementById('btn-run').style.display = 'none'
    }
    ipcRenderer.on('finished-py', (event) => {
        document.getElementById('loading').style.display = 'none'
        document.getElementById('run').style.display = 'block'
    });
    return (
        <div className="run">
            <button className='btn btn-danger' id='btn-run' onClick={run} style={{ width: '100%', display: 'block' }} >Rodar</button>
            <div class="text-center" id='loading' style={{ display: 'none' }}>
                <div class="spinner-border text-danger" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>
        </div>
    )
}