import React from 'react';
import {Form, Button} from 'react-bootstrap';

function PurchaseAdd() {
    return (
        <div className="container">
           <Form>
  <Form.Group controlId="samankoname">
    <Form.Label>सामान को नाम:
</Form.Label>
    <Form.Control type="text" placeholder="सामान को नाम:" />
    
  </Form.Group>

  <Form.Group controlId="kinekoprice">
    <Form.Label>किनेको मुल्य (१ को):</Form.Label>
    <Form.Control type="number" placeholder="किनेको मुल्य (१ को)" />
  </Form.Group>
  <Form.Group controlId="katiwata">
    <Form.Label>कती वटा :
:</Form.Label>
    <Form.Control type="text" placeholder="कती वटा :
" />
  </Form.Group>
  <Form.Group controlId="kinekoprice">
    <Form.Label>कताबाट किनेको ?:</Form.Label>
    <Form.Control type="text" placeholder="कताबाट किनेको ?" />
  </Form.Group>
 
  <Form.Group controlId="dinabaaki">
    <Form.Label>दिन बाँकी :
</Form.Label>
    <Form.Control type="number" placeholder="तपाईंले उता कती पैसा दिन बाँकी छ ? छैन भने खाली छोड् दिनु होश 
" />
  </Form.Group>
 
  <Button variant="success" type="submit">
    Send ▶ 
  </Button>
</Form>
        </div>
    )
}

export default PurchaseAdd
