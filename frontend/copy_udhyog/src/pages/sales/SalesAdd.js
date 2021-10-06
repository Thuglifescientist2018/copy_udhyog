import React from 'react';
import {Form, Button} from 'react-bootstrap';

function PurchaseAdd() {
  const getCookie = (name)  => {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
  const handleFormSubmit = (e) => {
    
    e.preventDefault()


    var csrftoken = getCookie('csrftoken')

    var url = 'http://127.0.0.1:8000/api/task-create/'

    


    fetch(url, {
      method:'POST',
      headers:{
        'Content-type':'application/json',
        'X-CSRFToken':csrftoken,
      },
      body:JSON.stringify(this.state.activeItem)
    }).then((response)  => {
        this.fetchTasks()
        this.setState({
           activeItem:{
          id:null, 
          title:'',
          completed:false,
        }
        })
    }).catch(function(error){
      console.log('ERROR:', error)
    })
  }
    return (
        <div className="container">
           <Form onSubmit={handleFormSubmit}>
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
