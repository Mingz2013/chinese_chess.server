/**
 * Created by zhaojm on 23/09/2016.
 */
import React, { Component, PropTypes } from 'react'
import {TAB_ACCOUNT, TAB_FRIENDS_LIST, TAB_MESSAGE} from '../../constants/TabIndex'

export default class BottomTabs extends Component {
    render() {


        return (
            <div>
                <span onClick={(e, TAB_MESSAGE) => this.handleClick(e, TAB_MESSAGE)}>message</span>
                <span onClick={(e, TAB_FRIENDS_LIST) => this.handleClick(e, TAB_FRIENDS_LIST)}>friends</span>
                <span onClick={(e, TAB_ACCOUNT) => this.handleClick(e, TAB_ACCOUNT)}>account</span>
            </div>
        )
    }

    handleClick(e, tab) {
        const { changeTab } = this.props;
        changeTab(tab)
    }
}