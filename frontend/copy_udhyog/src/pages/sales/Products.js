import React from 'react';
import {Card, Button} from 'react-bootstrap';

function Products({products}) {
    return (
        <div>
              <div className="container" style={{overflowY: "scroll", minHeight: "500px", maxHeight: "800px"}}>
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
                <Button variant="secondary" className="mr-2">Edit</Button>
                <Button variant="danger">Delete</Button>
            </Card.Body>
            </Card>
            ))}
            </ul>
        </div>
        </div>
    )
}

export default Products
