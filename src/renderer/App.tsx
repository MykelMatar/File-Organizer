import {MemoryRouter as Router, Route, Routes} from 'react-router-dom';
import './App.css';
import FileBrowser from "./FileBrowser";

const Hello = () => {
    return (
        <div className="flex w-screen h-screen bg-white dark:bg-primary">
            <FileBrowser/>
        </div>
    );
};

export default function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Hello/>}/>
            </Routes>
        </Router>
    );
}
