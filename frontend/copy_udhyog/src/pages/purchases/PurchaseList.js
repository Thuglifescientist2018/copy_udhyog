import React, {useState, useEffect} from 'react';
import {Card, Button} from 'react-bootstrap';
import styled from 'styled-components';



function PurchaseList() {
    const [products, setProducts] = useState(null);
    const [totalprice, setTotalprice] = useState(0);
    const [count, setCount] = useState(0);
    const [loading, setLoading] = useState(true);
    useEffect(() => {
        const getProducts = async() => {
            const response = await fetch('http://127.0.0.1:8000/api/purchase-list');
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
        <Container>
            <Menu>
                <ul style={{margin: "10px"}}>
               <h4> जम्मा सामानहरु: {count}</h4>

               <h4>  जम्मा मुल्य: रु. {parseFloat(totalprice).toFixed(2)}</h4>
                </ul>
                <ul class="m-5">
                    <li>Purchase List</li>
                    <li>Add Purchases</li>
                </ul>
            </Menu>

        <Products className="container" style={{overflowY: "scroll", minHeight: "500px", maxHeight: "800px"}}>
            <ul>
            {products.map((product) => (

            <Card style={{marginTop: "10px"}}>
            <Card.Body>
                <Card.Title>{product.product_name}</Card.Title>
                <Card.Text>
                    <p>
                        {product.bought_from} बाट किनेको

                    </p>
                <p>{product.quantity} वटाको Price: रु.{parseFloat(product.price).toFixed(2) * parseFloat(product.quantity).toFixed(2)} </p>
                <p>एउटाको Price: रु. {parseFloat(product.price).toFixed(2)}</p>
                <p>Published on: {product.date}</p>
                </Card.Text>
                <Button variant="primary">Go somewhere</Button>
            </Card.Body>
            </Card>
            ))}
            </ul>
        </Products>
        </Container>
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

const Products = styled.section``


