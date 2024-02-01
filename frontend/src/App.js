import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Login from './components/Login';
import Signup from './components/Signup';
import CountiesComponent from './pages/Counties';
import Apartments from './components/Apartments';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login/>} />
        <Route path="/signup" element={<Signup/>} />
        <Route path="/dashboard" element={<Dashboard/>} />
        <Route path="/counties" element={<CountiesComponent/>} />
        <Route path="/counties/:county/apartments" element={<Apartments/>} />
      </Routes>
    </Router>
  );
}

export default App;
