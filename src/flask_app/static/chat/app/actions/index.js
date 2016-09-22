import { CHANGE_PAGE, ADD_CHAT } from '../constants/ActionTypes'

export const addChat = (text) => ({
    type: ADD_CHAT,
    text
});

export const changePage = (page) => ({
    type: CHANGE_PAGE,
    page
});