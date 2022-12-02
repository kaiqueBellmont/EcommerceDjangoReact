import React, { useEffect } from "react";
import {Link,useSearchParams, useParams,useNavigate,} from "react-router-dom";
import {Row,Col,ListGroup,Image,Form,Button,Card,} from "react-bootstrap";
import Message from "../components/Message";
import { addToCart, removeFromCart } from "../actions/cartActions";
import { useDispatch, useSelector } from "react-redux";
 
 
function CartScreen() {
    const navigate = useNavigate();
    const { id } = useParams();
    const [searchParams, setSearchParams] = useSearchParams();
    const qty = Number(searchParams.get("qty"));
    const dispatch = useDispatch();
    const cart = useSelector((state) => state.cart);
    const { cartItems } = cart;
  
 
    useEffect(() => {
        if (id) {
            dispatch(addToCart(id, qty));
        }
    }, [dispatch, id, qty]);
 
 
    const removeFromCartHandler = (id) =>{
        dispatch(removeFromCart(id))
    }
 
    const checkoutHandler = () =>{
        navigate(`/login?redirect=shipping`);
    }
 
    return (
        <Row>
            ...
        </Row>
    );
}
 
export default CartScreen;