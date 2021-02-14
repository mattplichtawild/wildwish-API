import axios from "axios";
import React, { useReducer } from "react";

// Use useReducer hook to control state of multiple form fields

function reducer(state, {field, value}) {
    return {
        ...state,
        [field]: value
    };
};

// Donate form should have props so :wishId can be inherited from list item key
function DonateForm(props) {
    // Use useReducer hook to control state of multiple form fields

    // find active wish and set as var
    let active_wish = props.animal.wish_set.filter(w => w.active=true)
    
    console.log(active_wish)

    const initialState = {
        first_name: '',
        last_name: '',
        email: '',
        amount: 1,
        wish_id: active_wish.id
    };
    const [state, dispatch] = useReducer(reducer, initialState);
    const handleChange = (e) => {
        dispatch({field: e.target.name, value: e.target.value})
    };
    const {first_name, last_name, email, amount, wish_id} = state;

    const handleSubmit = (e) => {
    // e.preventDefault();
    // POST to /donations to create new donation, params sent: :wish_id
    // TODO: POST :first_name, :last_name, :email to /users to create new user

    // TODO: Refactor to function so this can be reused elsewhere like createDonation(:wishId)

    // Use more RESTful url. Create serializer to handle POST requests to /donations
    axios.post('/donations', {
        state
    })
    console.log('Donation Submitted!')
    // how to close modal?
    };

    return (
        <form onSubmit={handleSubmit}>
        <label htmlFor="first_name">First Name</label>
        <p>Wish ID:</p>
        <p>{active_wish.id}</p>
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
        <label htmlFor="email">Email</label>
        <input
            className="email"
            type="email"
            name="email"
            placeholder="Email"
            value={email}
            onChange={handleChange}
        ></input>
        <button>Donate</button>
        </form>
    );
}

export default DonateForm;