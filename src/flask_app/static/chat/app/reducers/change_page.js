import { CHANGE_PAGE } from '../constants/ActionTypes'
import { LOGIN } from '../constants/PageTypes'

export function change_page(state = LOGIN, action) {
    switch (action.type) {
        case CHANGE_PAGE:
            return action.page;
        default:
            return state
    }
}
