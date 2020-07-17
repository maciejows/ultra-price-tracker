import { createAction, props } from '@ngrx/store';
import { SearchedItem } from '../models/SearchedItem';

export const searchProduct = createAction('[Search Component] Search product', props<{searchingPhrase: string}>());
export const getItem = createAction('[Search Component] Get Item', props<{item: SearchedItem}>())