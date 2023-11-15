import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Index from './index';
import Aptitude from './aptitude';
import Projects from './projects';

const AppRouter = () => {
    return (
        <Router>
            <Switch>
                <Route path="/" exact component={Index} />
                <Route path="/aptitude" component={Aptitude} />
                <Route path="projects" component={Projects}/>
            </Switch>
        </Router>
    );
};

export default AppRouter;