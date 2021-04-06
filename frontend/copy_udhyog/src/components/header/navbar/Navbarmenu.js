import React from 'react';
import {Navbar, Nav, Form, FormControl, Button} from  'react-bootstrap';
import { Link } from 'react-router-dom';

function Navbarmenu() {
    return (
        <Navbar bg="light" expand="lg">
          <Navbar.Brand href="#home">आरती कपि उध्योग</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Link>
                  <Link className="text-secondary" to="/">Home</Link>
              </Nav.Link>
              <Nav.Link>
                  <Link className="text-secondary" to="/purchases">Purchases</Link>
              </Nav.Link>
              <Nav.Link>

                  <Link className="text-secondary" to="/sales">Sales</Link>
              </Nav.Link>
              
            </Nav>
            <Form inline>
              <FormControl type="text" placeholder="Search" className="mr-sm-2" />
              <Button variant="outline-success">Search</Button>
            </Form>
        </Navbar.Collapse>
</Navbar>
    )
}

export default Navbarmenu