import React from 'react';
import './App.css';
import Header from './components/Header';
import FeaturedHouse from './components/featuredHouse';
import HouseFilter from './components/houseFilter';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      
    }
  }

  componentDidMount() {
    this.fetchHouses();
  }

  fetchHouses = () => {
    fetch('./houses.json')
    .then(resp => resp.json())
    .then(allHouses => {
      this.allHouses = allHouses;
      this.getFeaturedHouse();
      this.getUniqueCountries();
    })
  }

  getUniqueCountries = () => {
    const countries = this.allHouses
      ? Array.from(new Set(this.allHouses.map(h => h.country)))
      : [];
    countries.unshift(null);
    this.setState({ countries });
  }

  getFeaturedHouse() {
    if(this.allHouses) {
      const randomIndex = Math.floor(Math.random() * this.allHouses.length);
      const featuredHouse = this.allHouses[randomIndex];
      this.setState({ featuredHouse });
    }
  }

  filterHouses = (country) => {
    this.setState({ activeHouse: null });
    const filteredHouses = this.allHouses.filter((h) => h.country === country);
    this.setState({ filteredHouses });
    this.setState({ country });
  }
  
  setActiveHouse = (house) => {
    this.setState({ activeHouse: house });
  }

  render() {
  return (
    <div className="App">
      <Header subtitle="Providin houses all over the world" />
      <HouseFilter countries={this.state.countries} filterHouses={this.filterHouses} />
      <FeaturedHouse house={this.state.featuredHouse} />
    </div>
  );
}
}

export default App;
