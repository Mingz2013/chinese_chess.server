import { ADD_CHAT } from '../constants/ActionTypes'

export const addChat = (text) => ({
    type: ADD_CHAT,
    text
});