import { createReducer, on } from '@ngrx/store';
import { getItem } from './product.actions';
import { SearchedItem } from '../models/SearchedItem';

export interface State {
    searchedItem: SearchedItem;
    //TODO:
    // Item list here
}

export const initialState: State = {
    searchedItem: {name: "", imgUrl: "", price: 0}
}

const _reducer = createReducer(initialState,
    on(getItem, (state, {item}) => ({...state, searchedItem: item}))
    )

export function reducer(state, action){
    return _reducer(state, action);
}