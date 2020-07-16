import { createReducer, on } from '@ngrx/store';
import { passProductname, getItem } from './product.actions';
import { SearchedItem } from '../models/SearchedItem';

export interface State {
    productName: string;
    searchedItem: SearchedItem;
    //TODO:
    // Item list here
}

export const initialState: State = {
    productName: "",
    searchedItem: {name: "", imgUrl: "", price: 0}
}

const _reducer = createReducer(initialState,
    on(passProductname, (state, {searchingPhrase}) => ({...state, productName: searchingPhrase })),
    on(getItem, (state, {item}) => ({...state, searchedItem: item}))
    )