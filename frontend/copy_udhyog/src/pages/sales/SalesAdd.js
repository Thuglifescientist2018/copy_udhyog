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
    <Form.Label>बेचेको  मुल्य (१ को):</Form.Label>
    <Form.Control type="number" placeholder="बेचेको  मुल्य (१ को)" />
  </Form.Group>
  <Form.Group controlId="katiwata">
    <Form.Label>कती वटा :
:</Form.Label>
    <Form.Control type="text" placeholder="कती वटा :
" />
  </Form.Group>
  <Form.Group controlId="kinekoprice">
    <Form.Label>कता बेचेको  ?:</Form.Label>
    <Form.Control type="text" placeholder="कताबाट बेचेको  ?" />
  </Form.Group>
 
  <Form.Group controlId="dinabaaki">
    <Form.Label>दिन बाँकी :
</Form.Label>
    <Form.Control type="number" placeholder="तपाईंले  कती पैसा लिन बाँकी छ ? छैन भने खाली छोड् दिनु होश 
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
