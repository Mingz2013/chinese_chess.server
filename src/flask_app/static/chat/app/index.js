import React from 'react'
import { render } from 'react-dom'
import { Provider } from 'react-redux'
import configureStore from './store/configureStore'
import App from './containers/App'
import rootReducer from './reducers'
import { createStore } from 'redux'

import createStoreWithMiddleware from './store/create'

import DevTools from './containers/DevTools';

//const store = createStore(rootReducer);
const store = createStoreWithMiddleware();

let rootElement = document.getElementById('app');
render(
    <Provider store={store}>
        <App />
        <DevTools />
    </Provider>,
    rootElement
)