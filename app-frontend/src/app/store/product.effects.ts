import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType} from '@ngrx/effects'
import { map, mergeMap, catchError } from 'rxjs/operators'
import { DataService } from '../services/data.service';
import { searchItem, searchItemSuccess, searchItemError } from '../store/product.actions';
import { of } from 'rxjs';

@Injectable()
export class ProductEffects {
    constructor(
        private actions$: Actions,
        private dataService: DataService
    ) {}

    getProposalItem$ = createEffect(() =>
        this.actions$.pipe(
            ofType(searchItem),
            mergeMap( action =>
                this.dataService.getItem(action.searchingPhrase).pipe(
                    map(item => searchItemSuccess({item})),
                    catchError(error => of(searchItemError({error: error})))
                )       
            )
        )
    );

    
}