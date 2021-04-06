import React, {useState, useEffect} from 'react';
import {Card, Button} from 'react-bootstrap';
import styled from 'styled-components';


function PurchaseList() {
    const [products, setProducts] = useState(null);
    const [loading, setLoading] = useState(true);
    useEffect(() => {
        const getProducts = async() => {
            const response = await fetch('http://127.0.0.1:8000/api/purchase-list');
            const data = await response.json();
            setProducts(data);
            setLoading(false);
        }
        getProducts();
    }, []);
    if(loading) return <h1>Loading...</h1>
    return (
        <Container>
            <Menu>
                <ul style={{margin: "10px"}}>
               <h4> जम्मा सामानहरु: {products.length}</h4>

               <h4>  जम्मा मुल्य: रु. 55914.55</h4>
                </ul>
            </Menu>

        <Products className="container" style={{overflowY: "scroll", height: "43%"}}>
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
grid-template-columns: 100px auto;
`

const Menu = styled.section``

const Products = styled.section``


