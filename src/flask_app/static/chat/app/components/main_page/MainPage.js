/**
 * Created by zhaojm on 23/09/2016.
 */
import React, { Component, PropTypes } from 'react'

import AccountTab from './account_tab/AccountTab'
import FriendsListTab from './friends_list_tab/FriendsListTab'
import MessageTab from './message_tab/MessageTab'
import BottomTabs from './BottomTabs'

export default class MainPage extends Component {
    render() {
        //const { dispatch, chats } = this.props;

        return (
            <div>
                <AccountTab/>
                <FriendsListTab/>
                <MessageTab/>
                <BottomTabs />
            </div>
        )
    }
}