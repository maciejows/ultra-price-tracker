import { createReducer, on } from '@ngrx/store';
import { searchItem, searchItemError, searchItemSuccess, clear } from './product.actions';
import { ItemState } from '../models/ItemState';


export const initialState: ItemState = {
    item: {
        _id: null,
        item_name: '',
        shops: []
    },
    error: ''
}

const _reducer = createReducer(initialState,
    on(searchItemSuccess, (state, {item}) => ({...state, item: item})),
    on(searchItemError, (state, {error}) => ({...state, error: error})),
    on(clear, (state) => ({...state, item: undefined}))
    )

export function reducer(state: ItemState, action){
    return _reducer(state, action);
}