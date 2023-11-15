import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Index from './index';
import Aptitude from './aptitude';
import Projects from './projects';

const AppRouter = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" exact component={Index} />
                <Route path="/aptitude" component={Aptitude} />
                <Route path="projects" component={Projects}/>
            </Routes>
        </Router>
    );
};

export default AppRouter;