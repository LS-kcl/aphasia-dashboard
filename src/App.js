import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import PageList from './pages/SetList';
import SetAdd from './pages/SetAdd';
import WriteParagraph from './pages/WriteParagraph'
import ViewPage from './pages/ViewPage';
import PickImages from './pages/PickImages';
import Home from './pages/Home'; 
import { Login } from './pages/Login';
import { SignUp } from './pages/Register';
import { setAuthToken } from './helpers/setAuthToken()';

// Check for JWT
const token = localStorage.getItem("token");
if (token) {
    setAuthToken(token);
}

function App() {
  return (
    <div className="App">
      <Router>
          <Routes>
              <Route exact path='/' element={<Home/>}/>
              <Route exact path='/login' element={<Login/>}/>
              <Route exact path='/sign_up' element={<SignUp/>}/>
              <Route exact path='/add_set' element={<SetAdd/>}/>
              <Route exact path='/browse' element={<PageList/>}/>
              <Route exact path='/write_paragraph' element={<WriteParagraph/>}/>
              <Route exact path='/view_page/:pageid' element={<ViewPage/>}/>
              <Route exact path='/pick_images/:pageid' element={<PickImages/>}/>
          </Routes>
      </Router>
    </div>
  );
}

export default App;
