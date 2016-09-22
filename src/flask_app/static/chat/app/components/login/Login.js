/**
 * Created by zhaojm on 23/09/2016.
 */
import React, { Component, PropTypes } from 'react'

export default class Login extends Component {
    render() {
        return (
            <div>
                <h1>Login</h1>
                username: <input type='text' ref='username'/><br/>
                password: <input type='text' ref='password'/><br/>
                <button onClick={(e) => this.handleClick(e)}>
                    login
                </button>
            </div>
        )
    }

    handleClick(e) {
        const username = this.refs.username;
        const username_text = username.value.trim();
        const password = this.refs.password;
        const password_text = password.value.trim();
        this.props.onLoginClick(username_text, password_text);
        //username.value = ''
    }
}