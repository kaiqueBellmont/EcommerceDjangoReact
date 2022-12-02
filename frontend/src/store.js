import { configureStore, combineReducers } from "@reduxjs/toolkit";
import thunk from "redux-thunk";
import {productListReducer,productDetailsReducer,} from "./reducers/productReducers";
import { cartReducer } from "./reducers/cartReducers";
 
const reducer = combineReducers({
    productList: productListReducer,
    productDetails: productDetailsReducer,
    cart: cartReducer,
});
 
const cartItemsFromStorage = localStorage.getItem("cartItem")
    ? JSON.parse(localStorage.getItem("cartItem"))
    : [];
 
 
export const initialState = 
{
    cart: { cartItems: cartItemsFromStorage },
};
 
 
const middleware = [thunk];
 
const store = configureStore({
    reducer: reducer,
    preloadedState: initialState,
    middleware: middleware,
});
 
export default store;