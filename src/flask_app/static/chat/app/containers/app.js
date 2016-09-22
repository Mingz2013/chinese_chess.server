import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { changePage, addChat } from '../actions/index'
import Login from '../components/login/Login'
import AddChat from '../components/AddChat'
import ChatList from '../components/ChatList'
import { LOGIN, MAIN } from '../constants/PageTypes'

class App extends Component {
    render() {
        const { dispatch, page_type, chats } = this.props;

        return (
            <div>
                {
                    page_type == LOGIN ?
                        (
                            <div>
                                <Login onLoginClick={(username, password) => dispatch(changePage(MAIN))}/>
                            </div>
                        )
                        :
                        (
                            <div>
                                <ChatList chats={chats}/>
                                <AddChat onAddClick={text => dispatch(addChat(text))}/>
                            </div>
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