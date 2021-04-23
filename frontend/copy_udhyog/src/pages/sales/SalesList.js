import React, {useState, useEffect} from 'react';
import styled from 'styled-components';
import {Route, Link, Switch, BrowserRouter as Router} from 'react-router-dom';
import Products from './Products';
import SalesAdd from './SalesAdd';

function PurchaseList() {
    const [products, setProducts] = useState(null);
    const [totalprice, setTotalprice] = useState(0);
    const [count, setCount] = useState(0);
    const [loading, setLoading] = useState(true);
    useEffect(() => {
        const getProducts = async() => {
            const response = await fetch('/api/sales-list/');
            const data = await response.json();
            setProducts(data[1]);
            setTotalprice(data[0].total);
            setCount(data[0].count);
            setLoading(false);
        }
        getProducts();
    }, []);
    if(loading) return <h1>Loading...</h1>
    return (
        <Router>
        <Container>
            <Menu>
                <ul style={{margin: "10px"}}>
               <h4> जम्मा सामानहरु: {count}</h4>

               <h4>  जम्मा मुल्य: रु. {parseFloat(totalprice).toFixed(2)}</h4>
                </ul>
                <ul class="m-5">
                    <li>
                        <Link to="/sales">
                        Sales List
                        </Link>
                    </li>
                    <li>
                        <Link to="/sales-add">
                        Add Sales
                        </Link>
                        
                        </li>
                </ul>
            </Menu>
             <Switch>
                 <Route  path="/sales">
                 <Products products={products}/>
                 </Route>
                 <Route path="/sales-add">
                     <SalesAdd/>
                 </Route>
             </Switch>

              
        
        </Container>
         </Router>
    )
}

export default PurchaseList;
const Container = styled.section`
display: grid;
grid-template-columns: 30% auto;
`
const Menu = styled.section`
        border: 3px solid gray;
        min-height: 88vh;
        border-radius: 20px;
        margin: 10px;
`