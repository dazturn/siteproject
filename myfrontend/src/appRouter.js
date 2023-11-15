import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ReactDOM from 'react-dom'

import Index from './index';
import Aptitude from './aptitude';
import Projects from './projects';

const AppRouter = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" exact element={<Index />} />
                <Route path="/aptitude" element={<Aptitude />} />
                <Route path="/projects" element={<Projects />}/>
            </Routes>
        </Router>
    );
};

// The following section creates the app's entrypoint.
ReactDOM.render(
    <React.StrictMode>
        <AppRouter />
    </React.StrictMode>,
    document.getElementById('root')
);

export default AppRouter;