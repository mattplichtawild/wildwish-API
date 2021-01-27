import React, { Component } from "react";
import { render } from "react-dom";
import WishCarousel from './WishCarousel'
import Landing from "./Landing"
import NavBar from "./NavBar";

// import axios from "axios";

// import { BrowserRouter as Router, Route } from 'react-router-dom';
import { HashRouter as Router, Route, Switch } from "react-router-dom";

import { makeStyles, createMuiTheme, ThemeProvider } from '@material-ui/core/styles'
import About from './About'

const theme = createMuiTheme();
    theme.typography.h1 = {
        fontSize: '2.5rem',
        '@media (min-width:600px)': {
            // fontSize: '1.5rem',
        },
        [theme.breakpoints.up('md')]: {
            fontSize: '4rem',
    },
};
// App contains theming to pass down to other components
// For router, basename="/static" ?

// Something about using HashRouter instead of BrowserRouter from 'react-router-dom' helps solve 404 requests
// where refreshing would cause browser to send request to that url. Prepends '#' to paths though...
export default function App() {

  return (
    <>
    <Router >
    <ThemeProvider theme={theme}>
    <NavBar />
    {/* Landing and WishCarousel could probably be clumped together in Home */}
    <Route exact path="/" component={Landing}/>
    <Route exact path="/animals" component={WishCarousel}/>
    <Route exact path="/about" component={About} />
    {/* <Landing /> */}
    {/* <WishCarousel /> */}
    </ThemeProvider>
    </Router>
    </>
  );
}