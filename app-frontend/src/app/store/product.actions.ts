import { createAction, props } from '@ngrx/store';
import { SearchedItem } from '../models/SearchedItem';

export const passProductname = createAction('[Search Component] Passing product name', props<{searchingPhrase: string}>());
export const getItem = createAction('[Search Component] Get Item', props<{item: SearchedItem}>())