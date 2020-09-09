import { createReducer, on } from '@ngrx/store';
import { searchItem, searchItemError, searchItemSuccess } from './product.actions';
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
    on(searchItemError, (state, {error}) => ({...state, error: error}))
    )

export function reducer(state: ItemState, action){
    return _reducer(state, action);
}