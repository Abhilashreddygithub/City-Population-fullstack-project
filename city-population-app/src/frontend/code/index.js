import React from 'react';
import { createRoot } from 'react-dom/client';
import App from '../src/node-js/App.js'; // Updated import path to use the updated App component
import './index.css';

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);
