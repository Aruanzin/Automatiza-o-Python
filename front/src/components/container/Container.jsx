import Entry from '../entry/Entry';
import Run from '../run/Run';
import Map from '../map/Map'
import fs from 'fs'
import { useEffect, useState } from 'react';

export default function Container() {
    const [data, setData] = useState({
        'localizacoes': [],
        'titulos': [],
        'descricao': [],
        'filePath': '',
        'map': ''
      })
    
      async function readPreviousData() {
        try {
          
          const jsonFile = fs.readFileSync('_data.json');
          const dataJson = JSON.parse(jsonFile)
          // parse the JSON data
          await setData(dataJson);
    
          console.log(data, 'arquivo encontrado')
        } catch (e) {
          const jsonFile = {
            'localizacoes': [],
            'titulos': [],
            'descricao': [],
            'filePath': '',
            'map': ''
          }
          const jsonData = JSON.stringify(jsonFile);
          fs.writeFileSync('_data.json', jsonData);
          console.log(jsonFile, 'arquivo não encontrado', e)
          await setData(jsonFile)
    
          // write the string to a file
    
        }
      }
    
      useEffect(() => {
        readPreviousData()
      }, [])
    return (
        <div className="container md-8">
            <Entry data={data['titulos']} type="title" title="Titulo da Localização"></Entry>
            <Entry data={data['localizacoes']} type="loc" title="Localização"></Entry>
            <Entry data={data['descricao']} type="desc" title="Descrição"></Entry>
            <Map />
            <Run></Run>
        </div>
    )
}