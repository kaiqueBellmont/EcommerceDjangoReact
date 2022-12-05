import React, {useState, useEffect} from 'react'
import { Button, Form } from 'react-bootstrap'
import { useSearchParams, useNavigate, useLocation } from "react-router-dom";
 
 
const useQuery = () => {
    return new URLSearchParams(useLocation().search);
}
 
 
function SearchBox() {
    const navigate = useNavigate();
    const location = useLocation();
    //console.log(location.pathname)  
 
    let q = useQuery().get("keyword")
    q = q ? q : ''
 
    const [keyword, setKeyword] = useState(q)
 
    console.log('q:'+q)
    console.log('keyword:'+keyword)
 
 
    useEffect(() => {
        setKeyword(q)
    }, [q])
 
 
    const submitHandler = (e) => {
        e.preventDefault()
 
        if(keyword) {
            navigate(`/?keyword=${keyword}&page=1`)
        }
        else {
            navigate(location.pathname)
        }
    }
 
    return (
        <Form onSubmit={submitHandler} className='d-flex'>
            <Form.Control
                type='text'
                name='q'
                value={keyword}
                onChange={(e) => setKeyword(e.target.value)}
                className='mr-sm-2 ml-sm-5 p-2'
            ></Form.Control>
 
            <Button
                type='submit'
                variant='outline-success'
                className='p-2 mx-md-1'
                //style={{"margin-left":"5px", "color":"red"}}
            >
                Submit
            </Button>
        </Form>
    )
}
 
export default SearchBox