import './App.css';
import Entry from './components/entry/Entry';
import Run from './components/run/Run';
import File from './components/file/File'
import Map from './components/map/Map'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
           MapMaker
        </p>
        
      </header>
      <Entry type="desc" title="Descrição"></Entry>
      <Entry type="loc" title="Localização"></Entry>
      <Entry type="title" title="Titulo da Localização"></Entry>
      <File/>
      <Map/>
      <Run></Run>
    </div>
  );
}

export default App;
