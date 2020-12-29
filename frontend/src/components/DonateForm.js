import React, { useReducer } from "react";

// Use useReducer hook to control state of multiple form fields

const initialState = {
    first_name: '',
    last_name: '',
    email: '',
    amount: 1,
};

function reducer(state, {field, value}) {
    return {
        ...state,
        [field]: value
    };
};

function DonateForm() {
    const [state, dispatch] = useReducer(reducer, initialState);
    const handleChange = (e) => {
        dispatch({field: e.target.name, value: e.target.value})
    };
    const {first_name, last_name, email, amount} = state;

    const handleSubmit = (e) => {
    // e.preventDefault();
    console.log('Donation Submitted!')
    // how to close modal?
    };

    return (
        <form onSubmit={handleSubmit}>
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