import React, { useState } from 'react'
import { ipcRenderer } from 'electron';
import './Entry.css'

export default function Entry(props) {
    const [values, setValues] = useState([])
    function handleKeyDown(event) {
        if (event.key === 'Enter') {
            // Run your function here
            setNewEntry()
        }
    }

    async function setNewEntry() {
        const entry = document.getElementById(props.type).value
        if (entry) {
            await setValues([...values, entry])
            console.log(values)
            ipcRenderer.send(`entry-${props.type}`, values);
            document.getElementById(props.type).value = ''
        }
    }
    async function updateEntry(index) {
        await setValues(() => {
            const newArray = [...values];
            newArray[index] = document.getElementById(`${props.type}-item-${index}`).value;
            console.log(newArray)
            return newArray;

        });
        console.log(values)
        ipcRenderer.send(`entry-${props.type}`, values);
    }
    function deleteEntry(i) {
        updateEntry(i)
        const filteredArray = values.filter((value, index) => index !== i);
        setValues(filteredArray);

        console.log(filteredArray, values)
        ipcRenderer.send(`entry-${props.type}`, values);
    }

    return (
        <div className='data-container mb-5'>
            <div className="entry mb-2">
                <div className="input-group">
                    <input type="text" id={`${props.type}`} onKeyDown={handleKeyDown}
                        className="form-control" placeholder={props.title} />
                    <button type="button" className="btn btn-primary"
                        onClick={e => setNewEntry(e)}>+</button>
                </div>
            </div>
            <div className="data">
                {
                    values.map((value, index) =>
                        <div className='mb-1 data-item input-group' key={index}>
                            <input type="text" id={`${props.type}-item-${index}`} onChange={() => updateEntry(index)} class="form-control" value={value} placeholder={props.title} />
                            <button type="button" className="btn btn-danger" onClick={() => deleteEntry(index)}>x</button>
                        </div>
                    )
                }
            </div>
        </div>
    )
}