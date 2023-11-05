import { useState, useEffect } from 'react' 

import MovieCard from './MovieCard';
import './App.css';
import SearchIcon from './search.svg';

const API_URL = 'http://www.omdbapi.com?apikey=18ec9893';

const movie = {
    "Title": "Batman",
    "Year": "1989",
    "imdbID": "tt0096895",
    "Type": "movie",
    "Poster": "https://m.media-amazon.com/images/M/MV5BMTYwNjAyODIyMF5BMl5BanBnXkFtZTYwNDMwMDk2._V1_SX300.jpg"
     
}

const App = () => {
    const [movies, setMovies] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [dateBegin, setDateBegin] = useState({varOne:new Date()})
    const [dateEnd, setDateEnd] = useState({varTwo:new Date()})
    const t_date = new Date().toISOString().split("T")[0];
    

    const searchMovies = async (title) => {
        const response = await fetch(`${API_URL}&s=${title}`)
        const data = await response.json();

        setMovies(data.Search);
    }

    useEffect(() => {
        searchMovies('Batman');

    }, []);

    return(
        <div className="app">
            <h1>Enter a Destination</h1>

            <div className="search">
                <input
                  className="placeholder"
                  placeholder="Enter a Location..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                />
                <div>
                    <label className="start_real">Start date: </label>
                    <input type="date" id="start" name="trip-start" min={t_date} max="2030-12-31" onChange ={(f) => setDateBegin(f.target.value)}/>
                </div>
                <div>
                    <label className="start_end">End date: </label>
                    <input type="date" id="start" name="trip-end" min={t_date} max="2030-12-31" onChange ={(f) => setDateEnd(f.target.value)}/>
                    
                </div>
                <img
                src={SearchIcon}
                alt="search"
                onClick={() => searchMovies(searchTerm)}
                />
            </div>

            {movies?.length > 0
            ? (
                <div className="container">
                {movies.map((movie) => (
                    <MovieCard movie={movie} />
                ))}
                </div> 
            ) : (
                <div className="empty">
                <h2>No movies found</h2>
                </div> 
            )}
        </div>
    );
}

export default App;
