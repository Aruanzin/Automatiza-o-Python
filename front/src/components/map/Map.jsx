import React, { useState } from 'react'
import { ipcRenderer } from 'electron';
import "./Map.css"

export default function Map() {
    const [fileSelected, setFileSelected] = useState('')
    
    function findFile(event) {
        const selectedFile = event.target.files[0];
        setFileSelected(selectedFile.name)
        console.log(selectedFile)
        ipcRenderer.send(`file-finder`, selectedFile.path);
    }
    function sendMapLink(){
        console.log(document.getElementById('map-input').value)
        ipcRenderer.send(`entry-map`, document.getElementById('map-input').value);
    }
    return (
        <div className='data-container mb-5'>
            <div className="entry mb-2">
                <div className="map-container w-100">
                    <label htmlFor="file" id='mapFile' >
                        <div className="input-group w-100">
                            <input type="text" id='fake-file'
                                className="form-control" placeholder={fileSelected ? fileSelected : 'Nenhum arquivo selecionado'}
                                readOnly
                                onClick={() => { document.getElementById('file').click() }} />
                            <button type="button" className={`btn text-white btn-${fileSelected ? 'warning' : 'primary'}`} onClick={() => { document.getElementById('file').click() }}
                            >{fileSelected ? 'Mudar Arquivo' : 'Adicionar arquivo'}</button>
                        </div>
                        <input type="file" class="form-control" onChange={(e) => findFile(e)} style={{ height: '58px', }} placeholder="" id="file" />
                    </label>
                </div>
            </div>
            <div className="entry">
                <input type="text" id='map-input' onChange={() => sendMapLink()} class="form-control" style={{height: '58px'}} placeholder='Link do mapa' />
            </div>
        </div>
    )
}