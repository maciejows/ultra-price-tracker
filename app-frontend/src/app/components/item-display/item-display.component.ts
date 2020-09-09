import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription, Observable } from 'rxjs';
import { Store } from '@ngrx/store';
import { ItemState } from 'src/app/models/ItemState';
import { searchItem } from '../../store/product.actions';
import { Item } from 'src/app/models/Item';

@Component({
  selector: 'app-item-display',
  templateUrl: './item-display.component.html',
  styleUrls: ['./item-display.component.scss']
})
export class ItemDisplayComponent implements OnInit {

  routeSub: Subscription;
  item$: Observable<Item>;
  error$: Observable<string>;

  constructor(
    private route: ActivatedRoute,
    private store: Store<{itemState: ItemState}>
    ) { }

  ngOnInit(): void {
    this.routeSub = this.route.queryParams.subscribe(
      params => {
        console.log(params['name']);
        this.store.dispatch(searchItem({searchingPhrase: params['name']}))
      }
    )

    this.item$ = this.store.select(state=> state.itemState.item);
    this.error$ = this.store.select(state=> state.itemState.error);
  }

  ngOnDestroy(): void {
    this.routeSub.unsubscribe();
  }

}
