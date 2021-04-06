import React from 'react';
import styled from 'styled-components';
import Navbarmenu  from './navbar/Navbarmenu';
import './header.css';


function Header() {
    return (
        <Container>
            <div id="header">
               <Navbarmenu/>
            </div>
        </Container>
    )
}

export default Header

const Container = styled.div`


`