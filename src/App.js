import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import PageList from './pages/SetList';
import SetAdd from './pages/SetAdd';
import WriteParagraph from './pages/WriteParagraph'
import ViewPage from './pages/ViewPage';
import Home from './pages/Home'; 

function App() {
  return (
    <div className="App">
      <Router>
          <Routes>
              <Route path='/' element={<Home/>}/>
              <Route path='/add_set' element={<SetAdd/>}/>
              <Route path='/browse' element={<PageList/>}/>
              <Route path='/write_paragraph' element={<WriteParagraph/>}/>
              <Route path='/view_page' element={<ViewPage/>}/>
              <Route path='/view_page/:pageid' element={<ViewPage/>}/>
          </Routes>
      </Router>
    </div>
  );
}

export default App;
