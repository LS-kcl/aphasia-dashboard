import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import PageList from './pages/SetList';
import SetAdd from './pages/SetAdd';
import WriteParagraph from './pages/WriteParagraph'

function App() {
  return (
    <div className="App">
      <Router>
          <Routes>
              <Route path='/' element={<SetAdd/>}/>
              <Route path='/browse' element={<PageList/>}/>
              <Route path='/write_paragraph' element={<WriteParagraph/>}/>
          </Routes>
      </Router>
    </div>
  );
}

export default App;
