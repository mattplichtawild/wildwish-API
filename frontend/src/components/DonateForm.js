import { Form } from "semantic-ui-react";
// src/components/Login.js

import React, { Component } from "react";

class DonateForm extends Component {
  state = {
    fields: {
      first_name: "",
      last_name: "",
      email: "",
      amount: 1,
    },
  };

  handleChange = (e) => {
    const newFields = { ...this.state.fields, [e.target.name]: e.target.value };
    this.setState({ fields: newFields });
  };

  handleLoginSubmit = (e) => {
    e.preventDefault();
    // whatever you want to do when user submits a form
  };

  render() {
    const { fields } = this.state;

    return (
          <form onSubmit={(e) => {
            this.handleLoginSubmit(e);
            this.props.handleClose();
           }}>
            <label htmlFor="first_name">First Name</label>
            <input
              className="first_name"
              type="text"
              name="first_name"
              placeholder="First Name"
              value={fields.first_name}
              onChange={this.handleChange}
            ></input>
            <label htmlFor="last_name">Last Name</label>
            <input
              className="last_name"
              type="text"
              name="last_name"
              placeholder="Last Name"
              value={fields.last_name}
              onChange={this.handleChange}
            ></input>
            <label htmlFor="email">Email</label>
            <input
              className="email"
              type="email"
              name="email"
              placeholder="Email"
              value={fields.email}
              onChange={this.handleChange}
            ></input>
            <button>Donate</button>
          </form>
    );
  }
}

export default DonateForm;