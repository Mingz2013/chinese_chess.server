import { CHANGE_PAGE, SEND_CHAT_MESSAGE } from '../constants/ActionTypes'

export const sendChatMessage = (message) => ({
    type: SEND_CHAT_MESSAGE,
    message
});

export const changePage = (page_index) => ({
    type: CHANGE_PAGE,
    page_index
});