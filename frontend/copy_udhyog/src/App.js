import Header from  './components/header/Header';
import Footer from  './components/footer/Footer';
import Purchases from  './pages/purchases/Purchases';
import Sales from  './pages/sales/Sales';
import Home from  './pages/home/Home';
import styled from 'styled-components';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
function App() {
  return (
    <div className="App">
     <Router>
       
          <Container>
            <Header/>
            <Main>
             
               <Switch>

               
                <Route exact path="/">
                  <Home/>
                </Route>
                <Route path="/purchases">
                  <Purchases/>
                </Route>
                <Route path="/sales">
                  <Sales/>
                </Route>

                
                </Switch>
               
           
            
            </Main>
            <Footer/>
          </Container>
        
      </Router>
    </div>
  );
}

export default App;
const Container = styled.div`
  width: 100%;
  height: 100vh;
  display: grid;
  grid-template-rows: 0.06fr auto 40px;
`

const Main = styled.div`
  display: grid;
  
  overflow: hidden;

` 