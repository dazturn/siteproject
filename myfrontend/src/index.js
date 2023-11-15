import React from 'react';
import { createRoot } from 'react-dom/client'
import AppRouter from './components/appRouter';


const root = document.getElementById('root');

const rootInstance = createRoot(root);
rootInstance.render(<AppRouter />);