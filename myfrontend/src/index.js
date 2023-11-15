import React from 'react';
import { createRoot } from 'react-dom'
import AppRouter from './appRouter';


const root = document.getElementById('root');

const rootInstance = createRoot(root);
rootInstance.render(<AppRouter />);