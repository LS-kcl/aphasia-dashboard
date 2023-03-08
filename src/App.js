import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import PageList from './components/SetList';
import SetAdd from './components/SetAdd';
import WriteParagraph from './components/WriteParagraph'

function App() {
  return (
    <div className="App">
      <Router>
          <Routes>
              <Route path='/' element={<PageList/>}/>
              <Route path='/browse' element={<SetAdd/>}/>
              <Route path='/write_paragraph' element={<WriteParagraph/>}/>
          </Routes>
      </Router>
    </div>
  );
}

export default App;
