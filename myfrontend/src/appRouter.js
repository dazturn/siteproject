import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ReactDOM from 'react-dom'

import Indexpage from './indexpage';
import Aptitude from './aptitude';
import Projects from './projects';

const AppRouter = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" exact element={<Indexpage />} />
                <Route path="/aptitude" element={<Aptitude />} />
                <Route path="/projects" element={<Projects />}/>
            </Routes>
        </Router>
    );
};

export default AppRouter;