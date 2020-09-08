import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType} from '@ngrx/effects'
import { map, mergeMap } from 'rxjs/operators'
import { DataService } from '../services/data.service';
import { searchProduct, getItem } from '../store/product.actions';

@Injectable()
export class ProductEffects {
    constructor(
        private actions$: Actions,
        private dataService: DataService
    ) {}

    getProposalItem$ = createEffect(() =>
        this.actions$.pipe(
            ofType(searchProduct),
            mergeMap( action =>
                this.dataService.getProposalItems(action.searchingPhrase).pipe(
                map(item => getItem({item}))
                )       
            )
        )
    );

    
}