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
              <Route exact path='/' element={<Home/>}/>
              <Route exact path='/add_set' element={<SetAdd/>}/>
              <Route exact path='/browse' element={<PageList/>}/>
              <Route exact path='/write_paragraph' element={<WriteParagraph/>}/>
              <Route exact path='/view_page/:pageid' element={<ViewPage/>}/>
          </Routes>
      </Router>
    </div>
  );
}

export default App;
