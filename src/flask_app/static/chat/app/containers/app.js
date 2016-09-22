import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { changePage, addChat } from '../actions/index'
import LoginPage from '../components/login/LoginPage'
import MainPage from '../components/main/MainPage'

import { LOGIN, MAIN } from '../constants/PageTypes'

class App extends Component {
    render() {
        const { dispatch, page_type, chats } = this.props;

        return (
            <div>
                {
                    page_type == LOGIN ?
                        (

                            <LoginPage onLoginClick={(username, password) => dispatch(changePage(MAIN))}/>

                        )
                        :
                        (
                            <MainPage dispatch={dispatch} chats={chats}/>
                        )
                }
            </div>
        )
    }
}

let mapStateToProps = (state) => ({
    page_type: state.page_type,
    chats: state.chats
});

export default connect(mapStateToProps)(App)