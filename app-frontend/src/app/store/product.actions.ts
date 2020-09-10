import { createAction, props } from '@ngrx/store';
import { Item } from '../models/Item';

export const searchItem = createAction('[Search Component] Get Item', props<{searchingPhrase: string}>());
export const searchItemSuccess = createAction('[Search Component] Get Item Success', props<{item: Item}>())
export const searchItemError = createAction('[Search Component] Get Item Error', props<{error: string}>())

export const clear = createAction('[Item Display Component] Clear');