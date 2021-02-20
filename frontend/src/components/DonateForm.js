import axios from "axios";
import React, { useReducer } from "react";
import Cookies from 'js-cookie';

// Set header in POST request to include csrf token
// axios.defaults.xsrfCookieName = 'csrftoken'
// axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.withCredentials = true

// Use useReducer hook to control state of multiple form fields
function reducer(state, {field, value}) {
    return {
        ...state,
        [field]: value
    };
};

// Donate form should have props so :wishId can be inherited from list item key
function DonateForm(props) {
    // let csrftoken = getCookie('csrftoken');
    let csrfToken = Cookies.get('csrftoken');

    
    // find active wish and set as var
    let activeWish = props.animal.wish_set.find(w => w.active=true)
    
    console.log(activeWish)
    
    const initialState = {
        first_name: '',
        last_name: '',
        email: '',
        amount: props.amount,
        wish_id: activeWish.id
    };
    // Use useReducer hook to control state of multiple form fields
    const [state, dispatch] = useReducer(reducer, initialState);
    const handleChange = (e) => {
      
        dispatch({field: e.target.name, value: e.target.value})
    };
    const {first_name, last_name, email, amount, wish_id} = state;

    const handleSubmit = (e) => {
        e.preventDefault();
        // POST to /donations to create new donation, params sent: :wish_id
        // TODO: POST :first_name, :last_name, :email to /users to create new user
        // TODO: Refactor to function so this can be reused elsewhere like createDonation(:wishId)
        axios.post('/donations/', 
            {
                // first_name, last_name, email, amount, wish_id
                first_name: first_name,
                last_name: last_name,
                email: email,
                amount: amount,
                wish_id: wish_id
            },
            {
                headers: {
                    "Content-Type": "application/json", 
                    'X-CSRFToken': csrfToken
                }
            }
        )
        .then(resp => {console.log(resp)})
        // how to close modal?
    };

    return (
        <form method="post" action="/donations/" onSubmit={handleSubmit}>
        <input type="hidden" name="csrfmiddlewaretoken" value={csrfToken} />
        <input type="hidden" name="wish_id" value={wish_id} />
        <label htmlFor="first_name">First Name</label>
        <input
            className="first_name"
            type="text"
            name="first_name"
            placeholder="First Name"
            value={first_name}
            onChange={handleChange}
        ></input>
        <label htmlFor="last_name">Last Name</label>
        <input
            className="last_name"
            type="text"
            name="last_name"
            placeholder="Last Name"
            value={last_name}
            onChange={handleChange}
        ></input>
        <br ></br>
        <label htmlFor="email">Email</label>
        <input
            className="email"
            type="email"
            name="email"
            placeholder="Email"
            value={email}
            onChange={handleChange}
        ></input>
        <p>Donating ${amount}</p>
        <label htmlFor="amount"/>
        <input id="amount" name="amount" value={amount} type="number" hidden readOnly/>
        <button type="submit" >Donate</button>
        </form >
    );
}

export default DonateForm;